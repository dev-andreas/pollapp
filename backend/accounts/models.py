from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username
