from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True)
    about_me = models.TextField(blank=True, null=True)
    unique_key = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        if self.date_of_birth:

            self.photo.field.upload_to = (
                f"{self.photo.field.upload_to}_{self.date_of_birth}/photo"
            )
        print(self.photo.url)
        super().save(*args, **kwargs)


class ContactModel(models.Model):
    user_from = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rel_from_set"
    )
    user_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rel_to_set"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"
