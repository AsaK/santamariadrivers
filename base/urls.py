from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create-driver/', views.CreateMotoristaView.as_view(), name='create-driver'),
    url(r'^list-drivers/', views.listmotoristaview, name='drivers'),
    url(r'^update-driver/(?P<pk>[0-9]+)', views.UpdateMotoristaView.as_view(), name='driver-update'),
    url(r'^delete-driver/(?P<pk>[0-9]+)', views.DeleteMotoristaView.as_view(), name='delete-driver'),
    url(r'^create-car/', views.UpdateMotoristaView.CreateCarroView.as_view(), name='create-car'),
    url(r'^list-cars/', views.UpdateMotoristaView.listcarroview, name='list-cars'),
    url(r'^update-car/(?P<pk>[0-9]+)', views.UpdateMotoristaView.UpdateCarroView.as_view(), name='update-car'),
    url(r'^delete-car/(?P<pk>[0-9]+)', views.UpdateMotoristaView.DeleteCarroView.as_view(), name='delete-car'),
]
