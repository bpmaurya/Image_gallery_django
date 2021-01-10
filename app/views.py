from django.shortcuts import redirect, render
from .models import Imagepost
from .form import Image_form
from django.core.files.base import ContentFile
# Create your views here.


def home(request):
    """
    docstring
    """
    imageposts = Imagepost.objects.all()
    return render(request, 'index.html',{'imageposts':imageposts})

def ImagePost(request,id):
    post = Imagepost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'imagepost.html',
                  {'post':post})


def Upload_image(request):
    form = Image_form(request.POST, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'upload_img.html', context) 

                  