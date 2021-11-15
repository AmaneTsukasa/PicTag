from django.db import models
from hashlib import md5


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    hash = models.CharField(max_length=200, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="images", blank=True)

    def __str__(self):
        return f'Image #{self.id}'

    def fill_metadata(self):
        self.width=self.image.width
        self.height=self.image.height
        self.hash=md5(self.image.read()).hexdigest()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
