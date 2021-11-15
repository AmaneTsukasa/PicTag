from django.views.generic import ListView

from .models import Image, Tag

class ImageListView(ListView):
    model = Image
    context_object_name = 'images'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if contxt['images']:
            id_list = [obj.id for obj in context['images']]
            context['tags'] = Tag.objects.filter(images__id__in=id_list).order_by('name').distinct()
        return context