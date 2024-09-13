from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from .models import Images, Tags, Changes
from .forms import AddTagForm, FilterForm
import os


# Returns a list of every element in the Images model.
def image_list(request, image_id=None):
    images = Images.objects.all()
    selected_image = None
    location_tags, time_tags, misc_tags = None, None, None

    if image_id:
        selected_image = get_object_or_404(Images, id=image_id)
        location_tags = selected_image.tags.filter(tag_type=Tags.LOCATION)
        time_tags = selected_image.tags.filter(tag_type=Tags.TIME)
        misc_tags = selected_image.tags.filter(tag_type=Tags.MISC)
    
    return render(request, 'gallery/image_list.html', {
        'images': images,
        'selected_image': selected_image,
        'location_tags': location_tags,
        'time_tags': time_tags,
        'misc_tags': misc_tags,
    })


# def image_list(request):
#     form = FilterForm(request.GET or None)
#     images = Images.objects.all()

#     if form.is_valid() and form.cleaned_data['tag']:
#         tag = form.cleaned_data['tag']
#         images = images.filter(tags=tag)
    
#     return render(request, 'gallery/image_list.html', {'images': images, 'form': form})


def serve_image(request, file_path):
    file_path = os.path.abspath(file_path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    else:
        raise Http404("File does not exist")


def image_detail(request, image_id):
    image = get_object_or_404(Images, id=image_id)
    location_tags = image.tags.filter(tag_type=Tags.LOCATION)
    time_tags = image.tags.filter(tag_type=Tags.TIME)
    misc_tags = image.tags.filter(tag_type=Tags.MISC)

    if request.method == 'POST':
        form = AddTagForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            image.tags.add(*tags)
            return redirect('image_detail', image_id=image.id)
    else:
        form = AddTagForm()
        
    return render(request, 'gallery/image_detail.html', {
        'image': image,
        'location_tags': location_tags,
        'time_tags': time_tags,
        'misc_tags': misc_tags,
        'form': form
    })


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