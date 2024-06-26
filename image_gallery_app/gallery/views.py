from django.shortcuts import render, redirect
from .models import Images
from .forms import ImageForm


def image_list(request):
    template = 'gallery/image_list.html'
    images = Images.objects.all()
    return render(request, template, {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})