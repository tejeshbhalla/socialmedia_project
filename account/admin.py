from django.contrib import admin
from .models import ProfileModel, ContactModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    pass
