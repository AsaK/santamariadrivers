# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista
from .forms import MotoristaForm


class MotoristaList(ListView):
    model = Motorista
    template_name = 'admin.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(MotoristaList, self).get_context_data(**kwargs)
        context['total_motoristas'] = Motorista.objects.all().count()
        context['motoristas_pendentes'] = Motorista.objects.filter(status='E').count()
        context['motoristas_aprovados'] = Motorista.objects.filter(status='A').count()
        context['motoristas_rejeitados'] = Motorista.objects.filter(status='R').count()
        return context




class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'
    form_class = MotoristaForm
    success_url = reverse_lazy('drivers')


def deletemotorista(request, idMotorista):

    if request.method == 'GET':

        if idMotorista:
            objMotorista = Motorista.objects.get(id=idMotorista)

            if objMotorista:
                objMotorista.delete()
                return redirect('drivers')

    return redirect('drivers')
