from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, age=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, age=age)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email=None, password=None, age=None):
        if not username:
            raise ValueError('An username is required.')
        if not password:
            raise ValueError('A password is required.')

        user = self.create_user(email, password, username, age)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    achievements = models.ManyToManyField('Achievement', related_name='users', blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()


    def __str__(self):
        return self.username


class Achievement(models.Model):
    achievement_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_gained = models.BooleanField(default=False)


    def __str__(self):
        return self.name