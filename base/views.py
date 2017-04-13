# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Motorista

# Create your views here.

class ListMotoristaView(ListView):
    model = Motorista

class UpdateMotoristaView(UpdateView):
    model = Motorista
    success_url = reverse_lazy('motorista_list')
    fields = ['__all__']

class DeleteMotoristaView(DeleteView):
    model = Motorista
    success_url = reverse_lazy('motorista_list')
