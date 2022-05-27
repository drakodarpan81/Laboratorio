from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombre, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tene un correo electrónico')

        usuario=self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellido
        )