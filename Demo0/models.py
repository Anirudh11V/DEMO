from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserReg(AbstractUser):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    phone = models.IntegerField(null=True)
    bio = models.TextField(max_length=200,null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
  