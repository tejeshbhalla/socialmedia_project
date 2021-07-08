from django import forms
from django.contrib.auth.models import User
from .models import ProfileModel


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ("date_of_birth", "photo", "about_me")
