from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    Dashboard,
    CustomPasswordChangeViewDone,
    CustomPasswordChangeView,
    CustomPassowordResetView,
    CustomPassowordResetDoneView,
    CustomPasswordConfirmView,
    CustomSignUp,
    Edit,
    view_profile,
    List_users,
)


app_name = "account"
urlpatterns = [  # path("login/", LoginView, name="login"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("", Dashboard, name="dashboard"),
    path("changepassword/", CustomPasswordChangeView.as_view(), name="passwordchange"),
    path(
        "changepassword/done/",
        CustomPasswordChangeViewDone.as_view(),
        name="passwordchangedone",
    ),
    path("reset_password/", CustomPassowordResetView.as_view(), name="passwordreset",),
    path(
        "reset_password/done",
        CustomPassowordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset_password/confirm/<uidb64>/<token>/",
        CustomPasswordConfirmView.as_view(),
        name="confirmview",
    ),
    path("sign_up/", CustomSignUp.as_view(), name="signup"),
    path("editprofile/", Edit, name="edit"),
    path("view_profile/<str:username>", view_profile, name="view_profile"),
    path("list_users/", List_users, name="list_users"),
]
