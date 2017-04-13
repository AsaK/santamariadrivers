# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Motorista
from .forms import MotoristaForm
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator


# Create your views here.


def listmotoristaview(request):
    status = request.GET.get('status', None)
    page = request.GET.get('page', None)
    queryset = Motorista.objects.all()
    paginator = Paginator(queryset, 10)
    if status:
        queryset = queryset.filter(status=status)
        paginator = Paginator(queryset, 2)
        if page:
            message = serializers.serialize("json", paginator.page(page))
        else:
            message = serializers.serialize("json", paginator.page(1))
        return HttpResponse(message, content_type="application/json")
    else:
        message = serializers.serialize("json", paginator.page(1))
        return HttpResponse(message, content_type="application/json")


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