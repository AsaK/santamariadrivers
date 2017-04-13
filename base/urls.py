from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list-drivers/', views.listmotoristaview, name='drivers'),
    url(r'^update-driver/(?P<pk>[0-9]+)', views.UpdateMotoristaView.as_view(), name='driver-update'),
    url(r'^delete-driver/(?P<pk>[0-9]+)', views.deletemotorista, name='delete-driver'),
    url(r'^create-car/', views.CreateCarroView.as_view(), name='create-car'),
    url(r'^update-car/(?P<pk>[0-9]+)', views.UpdateCarroView.as_view(), name='update-car'),
    url(r'^delete-car/(?P<pk>[0-9]+)', views.deletecarro, name='delete-car'),
]
