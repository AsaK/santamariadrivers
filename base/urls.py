from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list-drivers', views.ListMotoristaView, name='drivers'),
    url(r'^update-driver', views.UpdateMotoristaView, name='driver-update'),
    url(r'^delete-driver', views.DeleteMotoristaView, name='delete-driver'),
]
