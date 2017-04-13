from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create-driver/', views.CreateMotoristaView.as_view(), name='create-driver'),
    url(r'^list-drivers/', views.ListMotoristaView, name='drivers'),
    url(r'^update-driver/(?P<pk>[0-9]+)', views.UpdateMotoristaView.as_view(), name='driver-update'),
    url(r'^delete-driver/(?P<pk>[0-9]+)', views.DeleteMotoristaView.as_view(), name='delete-driver'),
]
