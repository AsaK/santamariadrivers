from django.shortcuts import render

# Create your views here.

from base.serializer import MotoristaSerializer
from base.models import Motorista

from rest_framework.response import Response
from rest_framework.views import APIView

# get requisição
