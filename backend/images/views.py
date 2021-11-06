from django.shortcuts import render

def image_list(request):
    return render(request, 'image/image_list.html', {})