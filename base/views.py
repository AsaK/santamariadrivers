# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista, Carro
from .forms import MotoristaForm
from django.http import HttpResponse

# Create your views here.


class CreateMotoristaView(CreateView):
    template_name = 'Motorista/motorista_register.html'
    form_class = MotoristaForm
    success_url = reverse_lazy('drivers')


def listmotoristaview(request):

    template_name = 'Motorista/motorista_list.html'
    # status = request.POST.get('data[status]')
    status = 'E'
    error = 'Error'

    if status:
        message = serializers.serialize("json", Motorista.objects.filter(status=status))
        return HttpResponse(message, content_type="application/json")
    else:
        return HttpResponse(error, content_type="application/json")


class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'

    def listcarroview(request):
        # trazer o carro do motorista, provavelmente usando a chave estrangeira (motorista) do carro.

        template_name = 'Carro/carro_list.html'
        motorista_id = request.POST.get('data[motorista_id]')

        if id:
            message = serializers.serialize("json",
                                            Carro.objects.filter(motorista=Motorista.objects.get(pk=motorista_id)))
            return HttpResponse(message, content_type="application/json")
        else:
            return HttpResponse('Nenhum carro cadastrado para este motorista.', content_type="application/json")

    class CreateCarroView(CreateView):
        model = Carro
        template_name = 'Carro/carro_register.html'

    class UpdateCarroView(UpdateView):
        model = Carro
        template_name = 'Carro/carro_update.html'

    class DeleteCarroView(DeleteView):
        model = Carro
        template_name = 'Carro/carro_delete.html'


class DeleteMotoristaView(DeleteView):
    model = Motorista
    template_name = 'Motorista/motorista_delete.html'


def listcarroview(request):
    # trazer o carro do motorista, provavelmente usando a chave estrangeira (motorista) do carro.

    template_name = 'Carro/carro_list.html'
    motorista_id = request.POST.get('data[motorista_id]')

    if id:
        message = serializers.serialize("json", Carro.objects.filter(motorista=Motorista.objects.get(pk=motorista_id)))
        return HttpResponse(message, content_type="application/json")
    else:
        return HttpResponse('Error', content_type="application/json")


