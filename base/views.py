# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista
from .forms import MotoristaForm
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json


# Create your views here.

class CreateMotoristaView(CreateView):
    template_name = 'Motorista/motorista_register.html'
    form_class = MotoristaForm
    success_url = reverse_lazy('drivers')

def ListMotoristaView(request):
    message = None
    template_name = 'Motorista/motorista_list.html'
    status = request.POST.get('data[status]')

    if status:

        message = Motorista.objects.filter(status=status)

    return JsonResponse(serializers.serialize('json',message), safe=False)

class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'


class DeleteMotoristaView(DeleteView):
    model = Motorista
    template_name = 'Motorista/motorista_delete.html'
