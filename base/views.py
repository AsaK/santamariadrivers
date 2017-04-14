# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template.loader import render_to_string

import tempfile
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .serializer import MotoristaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Motorista
from .forms import MotoristaForm


class MotoristaList(ListView):
    model = Motorista
    template_name = 'admin.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MotoristaList, self).get_context_data(**kwargs)
        context['total_motoristas'] = Motorista.objects.all().count()
        context['motoristas_pendentes'] = Motorista.objects.filter(status='E').count()
        context['motoristas_aprovados'] = Motorista.objects.filter(status='A').count()
        context['motoristas_rejeitados'] = Motorista.objects.filter(status='R').count()
        return context

    def get_queryset(self):
        queryset = super(MotoristaList, self).get_queryset()
        status = self.request.GET.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

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


class MotoristaListView(APIView):
    serializer_class = MotoristaSerializer

    def get(self,request, format=None):
        serializer = self.serializer_class(Motorista.objects.all(), many=True)
        return Response(serializer.data)