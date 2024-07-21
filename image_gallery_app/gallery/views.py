from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from .models import Images, Changes
import os


# Returns a list of every element in the Images model.
def image_list(request):
    images = Images.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})


def serve_image(request, file_path):
    file_path = os.path.abspath(file_path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    else:
        raise Http404("File does not exist")


def image_detail(request, image_id):
    image = get_object_or_404(Images, id=image_id)
    return render(request, 'gallery/image_detail.html', {'image': image})


def change_list(request):
    changes = Changes.objects.all()
    return render(request, 'gallery/change_list.html', {'changes': changes})


def handle_change(request, change_id):
    change = Changes.objects.get(id=change_id)

    if request.method == 'POST':
        if 'accept' in request.POST:
            if change.change_type == 'delete':
                # Remove image entry from database
                Images.objects.filter(file_path=change.file_path).delete()
            elif change.change_type == 'update':
                # Logic for handling updates (if any)
                pass
            # Remove the change entry after handling
            change.delete()
        elif 'reject' in request.POST:
            # Simply remove the change entry without any action
            change.delete()
        return redirect('change_list')

    return render(request, 'gallery/handle_change.html', {'change': change})