from django.shortcuts import render, get_object_or_404
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import ProfileModel
from .forms import UpdateUserForm, ProfileEditForm
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


# user_home_dashboard_view
def Dashboard(request, *args):
    return render(request, "accounts/dashboard.html", context={"section": "dashboard"})


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts:dashboard")
    success_message = "Successfully Logged In"


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    template_name = "accounts/logout.html"
    redirect_url = reverse_lazy("accounts:login")
    success_message = "Successfully Logged Out"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("account:passwordchangedone")


class CustomPasswordChangeViewDone(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class CustomPassowordResetView(PasswordResetView):
    template_name = "accounts/password_reset_view.html"
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("account:password_reset_done")


class CustomPassowordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_view_done.html"


class CustomPasswordConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:login")
    success_message = "Password Reset Done , You Can Now Sign In"

    def get_success_url(self):
        return reverse_lazy("account:login")


class CustomSignUp(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("account:login")
    template_name = "accounts/signup.html"
    success_message = "Successfully Signed Up"

    def form_valid(self, form):
        user = form.save()
        ProfileModel.objects.create(user=user)

        return super().form_valid(form)


# fbv for edit profile


@login_required()
def Edit(request):
    if request.method == "POST":
        user_form = UpdateUserForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Edited Profile Successfully")
        else:
            messages.error(
                request,
                f"Profile Edit Failed {user_form.errors} {profile_form.errors}",
            )

    user_form = UpdateUserForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit.html",
        context={"user_form": user_form, "profile_form": profile_form,},
    )


@login_required()
def view_profile(request, username):

    user = get_object_or_404(User, username=username, is_active=True)
    own_profile = False
    if user == request.user:
        own_profile = True
    if user.profile.date_of_birth:
        age = timezone.now().year - user.profile.date_of_birth.year
    age = 0
    return render(
        request,
        "accounts/view_profile.html",
        context={
            "user_profile": user.profile,
            "user": user,
            "age": age,
            "own_profile": own_profile,
        },
    )


@login_required()
def List_users(request):
    users = (
        User.objects.filter(is_active=True)
        .exclude(username=request.user.username)
        .all()
    )
    return render(request, "accounts/users_list.html", context={"users": users})
