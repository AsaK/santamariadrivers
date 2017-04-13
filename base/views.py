# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Motorista

# Create your views here.

class CreateMotoristaView(FormView):


class ListMotoristaView(ListView):
    model = Motorista
    template_name = 'Motorista/motorista_list.html'

class UpdateMotoristaView(UpdateView):
    model = Motorista
    template_name = 'Motorista/motorista_update.html'


class DeleteMotoristaView(DeleteView):
    model = Motorista
    template_name = 'Motorista/motorista_delete.html'
