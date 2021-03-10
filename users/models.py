from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["nmEmail"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        kwargs.update({'nmPerfil': 3})
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class ecdtUsuario(PermissionsMixin, AbstractBaseUser):
    PERFIS = [
        (1, 'Junior'), 
        (2, 'Pleno'), 
        (3, 'Sênior'),
    ]

    idUsuario = models.CharField(max_length=7, primary_key=True)
    nmUsuario = models.CharField(max_length=80)
    nmEmail = models.CharField(max_length=50, unique=True)  
    nmPerfil = models.IntegerField(choices=PERFIS)
    
    objects = EmailUserManager()
    USERNAME_FIELD = 'nmEmail'
    
    # Custom User
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.idUsuario
