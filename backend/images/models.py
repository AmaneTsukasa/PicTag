from django.db import models


class Image(models.Model):
    path = models.ImageField(upload_to="images")
    hash = models.CharField(max_length=200)
    height = models.IntegerField()
    width = models.IntegerField()
    tags = models.ManyToManyField("Tag", related_name="images")


class Tag(models.Model):
    name = models.CharField(max_length=50)
