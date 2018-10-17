from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo


def add_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # photo = Photo()
            # photo.save()
            photo_instance = form.save()
            # print("{}",photo.path)
            # return redirect('/photo/' + photo.id)
            return render(request, 'show-photo.html', {'photo_instance': photo_instance})
    else:
        form = PhotoForm()
    return render(request, 'add-photo.html', {'form': form})

def show_photo(request):
    photo = Photo.objects.get(id=id)
    print("{}", photo.image.public_id)
    return render(request, 'show-photo.html', {'photo': photo})
