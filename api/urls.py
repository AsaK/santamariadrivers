from django.conf.urls import url
from api.views import MotoristaListView

helper_patterns = [
    url(r'^apimotorista/$', MotoristaListView.as_view(), name='apimotorista'),
]

urlpatterns = helper_patterns
