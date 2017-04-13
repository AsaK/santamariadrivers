from django.forms import ModelForm
from .models import Motorista


class MotoristaForm(ModelForm):

    class Meta:
        model = Motorista
        fields = '__all__'