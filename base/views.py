# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista
from .forms import MotoristaForm
from django.http import HttpResponse,JsonResponse
from django.core import serializers


# Create your views here.

class CreateMotoristaView(CreateView):
    template_name = 'Motorista/motorista_register.html'
    form_class = MotoristaForm
    success_url = reverse_lazy('drivers')

def ListMotoristaView(request):
    template_name = 'Motorista/motorista_list.html'
    status = request.POST.get('data[status]')

    if status:

        message = serializers.serialize(Motorista.objects.filter("json",status=status))

        return JsonResponse(message, content_type='application/json')
    else:
        return HttpResponse('Error')
    
class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'


class DeleteMotoristaView(DeleteView):
    model = Motorista
    template_name = 'Motorista/motorista_delete.html'
