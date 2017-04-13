from django.conf.urls import url

from .views import listmotoristaview, UpdateMotoristaView, deletemotorista

urlpatterns = [
    url(r'^list-drivers/', listmotoristaview, name='drivers'),
    url(r'^update-driver/(?P<pk>[0-9]+)', UpdateMotoristaView.as_view(), name='driver-update'),
    url(r'^delete-driver/(?P<pk>[0-9]+)', deletemotorista, name='delete-driver'),
]
