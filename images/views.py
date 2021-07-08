from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ImageModel

# Create your views here.


@login_required
def Upload_image(request):

    if request.method == "POST":
        form = ImageUploadForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            if len(new_item.url) == 0:
                messages.warning(request, "Please add a valid image url")
                return redirect("images:upload_image")
            else:
                messages.success(request, "Image Uploaded Successfully")

                return redirect(new_item.get_absolute_url())
    form = ImageUploadForm(data=request.GET)
    return render(request, "images/upload_image.html", context={"form": form})


def Detail_image(request, slug, id):
    image = get_object_or_404(ImageModel, id=id, slug=slug)
    return render(
        request,
        "images/detail_image.html",
        context={"image": image, "section": "image"},
    )


@login_required
def ListUserImages(request):
    all_images = ImageModel.objects.filter(user=request.user)

    return render(request, "images/list_images.html", context={"images": all_images})
