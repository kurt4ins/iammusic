from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, spotify_id, display_name=None, email=None, **kwargs):
        if not spotify_id:
            raise ValueError("User must have a Spotify ID")

        user = self.model(
            spotify_id=spotify_id, display_name=display_name, email=email, **kwargs
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, spotify_id, display_name=None, email=None):
        user = self.create_user(spotify_id, display_name, email)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    spotify_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)

    spotify_access_token = models.CharField(max_length=500, blank=True)
    spotify_refresh_token = models.CharField(max_length=500, blank=True)
    spotify_token_expires = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "spotify_id"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.spotify_id} - {self.display_name}"
