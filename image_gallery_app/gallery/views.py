from django.shortcuts import render
# from django.http import HttpResponse
from .models import Images


# def members(request):
#     return HttpResponse("Hello World!")

def image_list(request):
    template = 'gallery/image_list.html'
    images = Images.objects.all()
    return render(request, template, {'images': images})
