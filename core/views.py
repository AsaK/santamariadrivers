# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView, RedirectView
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, HttpResponse
from base.models import Motorista, Usuario
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


def RegisterView(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # Carregar os campos
        nome = request.POST.get('name', None)
        email = request.POST.get('email', None)
        senha = request.POST.get('password', None)
        celular = request.POST.get('celular', None)
        dtnasc = request.POST.get('dtnasc', None)
        rg = request.POST.get('rg', None)
        orgao_emissor = request.POST.get('orgaoemissor', None)
        cpf = request.POST.get('cpf', None)
        endereco = request.POST.get('endereco', None)
        arquivo_foto = request.FILES['arquivo_foto']
        ncnh = request.POST.get('ncnh', None)
        dtcnhval = request.POST.get('dtcnhval', None)
        cnh_expedicao = request.POST.get('dtcnhexp', None)
        modelo = request.POST.get('automovel_modelo', None)
        ano = request.POST.get('automovel_ano', None)
        placa = request.POST.get('automovel_placa', None)
        cor = request.POST.get('automovel_cor', None)
        carro_foto = request.FILES['arquivo_foto_automovel']
        cnhA = request.POST.get('checkboxA', None)
        if cnhA:
            cnhA = 'A'
        cnhalt = request.POST.get('radio1', None)


        try:
            objUsuario = Usuario.objects.get(email=email)
            if objUsuario:
                messages.add_message(request, messages.ERROR, 'Já existe um usuário cadastrado com esse Email')
        except Usuario.DoesNotExist:
            objUsuario = None
        if not objUsuario:
            objUsuario = Usuario.objects.create_user(email, senha)
            objUsuario.nome = nome
            # Motorista
            objUsuario.tipo = 'M'
            objUsuario.save()

            objMotorista = Motorista()
            objMotorista.nome = nome
            objMotorista.cpf = cpf
            objMotorista.rg = rg
            objMotorista.orgao_emissor = orgao_emissor
            objMotorista.usuario = objUsuario
            objMotorista.data_nascimento = dtnasc
            objMotorista.celular = celular
            objMotorista.endereco = endereco
            objMotorista.cnh_numero = ncnh
            objMotorista.cnh_validade = dtcnhval
            objMotorista.cnh_primeira = cnh_expedicao
            objMotorista.modelo = modelo
            objMotorista.ano = ano
            objMotorista.cor = cor
            objMotorista.placa = placa
            objMotorista.cnh_categoria = '{0}'.format(cnhA + cnhalt)

            fileSystem =FileSystemStorage()
            fileName = fileSystem.save(arquivo_foto.name, arquivo_foto)
            fileUrl = fileSystem.url(fileName)
            objMotorista.foto = fileUrl

            fileSystem = FileSystemStorage()
            fileName = fileSystem.save(carro_foto.name, carro_foto)
            fileUrl = fileSystem.url(fileName)
            objMotorista.foto_carro = fileUrl

            objMotorista.status = 'E'

            objMotorista.save()

            return render(request, '')