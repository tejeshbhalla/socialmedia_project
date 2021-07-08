from django.urls import path
from .views import Upload_image, Detail_image, ListUserImages


app_name = "images"
urlpatterns = [
    path("upload_image", Upload_image, name="upload_image"),
    path("detail_image/<int:id>/<slug:slug>", Detail_image, name="detail_image"),
    path("list_image", ListUserImages, name="list_image"),
]
