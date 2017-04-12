# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Cria e salva um usuario.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Cria e salva um super usuario.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_admin = models.BooleanField(default=False, verbose_name='Administrador')

    USERNAME_FIELD = 'email'
    objects = UserManager()
    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def __str__(self):
        return self.email

    def has_perm(selfself, perm, obj=None):
        return True

    def has_module_perms(selfself, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
