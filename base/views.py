# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista, Carro
from .forms import MotoristaForm, CarroForm
from django.http import HttpResponse


# Create your views here.


def listmotoristaview(request):
    template_name = 'Motorista/motorista_list.html'
    status = request.POST.get('data[status]')
    if status:
        message = serializers.serialize("json", Motorista.objects.filter(status=status))
        return HttpResponse(message, content_type="application/json")
    else:
        message = serializers.serialize("json", Motorista.objects.all())
        return HttpResponse(message, content_type="application/json")


class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'
    form_class = MotoristaForm
    success_url = reverse_lazy('drivers')


class CreateCarroView(CreateView):
    model = Carro
    template_name = 'Carro/carro_register.html'


class UpdateCarroView(UpdateView):
    model = Carro
    form_class = CarroForm
    template_name = 'Carro/carro_update.html'


def deletecarro(request, idCarro):

    if request.method == 'GET':

        if idCarro:
            objCarro = Carro.objects.get(id=idCarro)

            if objCarro:

                Carro.delete()
                return redirect('drivers')

    return redirect('drivers')


def deletemotorista(request, idMotorista):

    if request.method == 'GET':

        if idMotorista:
            objMotorista = Motorista.objects.get(id=idMotorista)

            if objMotorista:
                objMotorista.delete()
                return redirect('drivers')

    return redirect('drivers')