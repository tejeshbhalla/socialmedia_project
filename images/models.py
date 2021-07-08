from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.


class ImageModel(models.Model):
    # fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_images")
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name="liked_images")
    date_published = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(default="media/defaults/user_default.jiff")

    class Meta:
        ordering = [
            "-date_published",
        ]

    def __str__(self):
        return f"Image  {self.title} by {self.user.username}"

    def get_absolute_url(self):
        return reverse("images:detail_image", args=[self.id, self.slug])
