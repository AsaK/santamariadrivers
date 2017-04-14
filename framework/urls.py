"""framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core.views import LoginView, LogoutView
from base.views import MotoristaList
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^dashboard$', MotoristaList.as_view(), name='dashboard'),
    url(r'^devadmin/', admin.site.urls, name='admin'),
    url(r'^motorista/', LoginView.as_view(template_name='login_motorista.html'), name='login_motorista'),
    url(r'^admin/', LoginView.as_view(template_name='login_admin.html'), name='login_admin'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^register/', TemplateView.as_view(template_name='register.html'), name='register'),
    url(r'^base/', include('base.urls')),
]
