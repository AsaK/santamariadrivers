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
    USER_TYPES = (
        ('F', 'Funcionário'),
        ('M', 'Motorista'),
    )
    tipo = models.CharField(max_length=1, default='F', choices=USER_TYPES, verbose_name='Tipo')

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

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Motorista(models.Model):
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    rg = models.CharField(max_length=10, verbose_name='RG')
    orgao_emissor = models.CharField(max_length=10, verbose_name='Orgão Emissor')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    cnh_numero = models.CharField(max_length=11, verbose_name='Número CNH')
    cnh_primeira = models.DateField(verbose_name='Primeira CNH')
    cnh_validade = models.DateField(verbose_name='Validade CNH')
    status_tipo = (
        ('E', 'Em Análise'),
        ('A', 'Aprovado'),
        ('R', 'Reprovado')
    )
    status = models.CharField(max_length=1, choices=status_tipo, verbose_name='Status')
    usuario = models.ForeignKey(
        'base.Usuario',
        on_delete=models.DO_NOTHING,
        verbose_name='Usuário'
    )
    foto = models.ImageField(
        verbose_name='Foto Perfil',
        upload_to='motoristas/'
    )

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

class Carro(models.Model):
    marca = models.CharField(max_length=30, verbose_name='Marca')
    modelo = models.CharField(max_length=30, verbose_name='Modelo')
    cor = models.CharField(max_length=10, verbose_name='Cor')
    placa = models.CharField(max_length=7, verbose_name='Placa')
    motorista = models.ForeignKey(
        'base.Motorista',
        on_delete=models.DO_NOTHING,
        verbose_name='Motorista'
    )
    foto = models.ImageField(
        verbose_name='Foto',
        upload_to='carros/'
    )

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'