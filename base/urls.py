from django.conf.urls import url

from .views import UpdateMotoristaView, deletemotorista, MotoristaList

urlpatterns = [
    url(r'^list-drivers/', MotoristaList, name='drivers'),
    url(r'^update-driver/(?P<pk>[0-9]+)', UpdateMotoristaView.as_view(), name='driver-update'),
    url(r'^delete-driver/(?P<pk>[0-9]+)', deletemotorista, name='delete-driver'),
]
