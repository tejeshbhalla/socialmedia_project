from django.contrib import admin
from .models import ImageModel

# Register your models here.
@admin.register(ImageModel)
class AdminImage(admin.ModelAdmin):
    exclude = ["likes"]
    list_display = ["user", "slug", "title", "description"]
