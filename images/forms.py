from .models import ImageModel
from django import forms
import requests
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ["title", "description", "url"]

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data["url"]
        name = slugify(image.title)
        image.slug = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f"{name}.{extension}"
        # download image from the given URL
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image
