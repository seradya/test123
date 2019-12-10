from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    comment = models.CharField(max_length=256)