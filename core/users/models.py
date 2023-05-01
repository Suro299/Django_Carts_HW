from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager
from main.models import Products 


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("User Name"), unique = True, max_length = 255, default = "")
    email = models.EmailField(_("email address"), blank = True, default = "" )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    cart_prod = models.ManyToManyField(Products) 

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} || {self.email}"