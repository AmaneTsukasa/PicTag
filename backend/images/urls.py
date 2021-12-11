from django.urls import path
from .views import ImageListView, TagAutocompleteView


app_name='images'

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('autocomplete/tags/', TagAutocompleteView.as_view(), name='tag-autocomplete'),
]