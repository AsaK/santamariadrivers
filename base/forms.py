from django.forms import ModelForm
from .models import Motorista, Carro


class MotoristaForm(ModelForm):

    class Meta:
        model = Motorista
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(MotoristaForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].widget.attrs['class'] = ''
        self.fields['cpf'].widget.attrs['placeholder'] = 'CPF'

        self.fields['rg'].widget.attrs['class'] = ''
        self.fields['rg'].widget.attrs['placeholder'] = 'RG'

        self.fields['orgao_emissor'].widget.attrs['class'] = ''
        self.fields['orgao_emissor'].widget.attrs['placeholder'] = 'Orgão Emissor'

        self.fields['data_nascimento'].widget.attrs['class'] = ''
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Data de Nascimento'

        self.fields['cnh_numero'].widget.attrs['class'] = ''
        self.fields['cnh_numero'].widget.attrs['placeholder'] = 'Número da CNH'

        self.fields['cnh_primeira'].widget.attrs['class'] = ''
        self.fields['cnh_primeira'].widget.attrs['placeholder'] = 'Primeira CNH'

        self.fields['cnh_validade'].widget.attrs['class'] = ''
        self.fields['cnh_validade'].widget.attrs['placeholder'] = 'Validade da CNH'


class CarroForm(ModelForm):

    class Meta:

        model = Carro
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(CarroForm, self).__init__(*args, **kwargs)

        self.fields['marca'].widget.attrs['class'] = ''
        self.fields['marca'].widget.attrs['placeholder'] = 'Marca'

        self.fields['modelo'].widget.attrs['class'] = ''
        self.fields['modelo'].widget.attrs['placeholder'] = 'Modelo'

        self.fields['cor'].widget.attrs['class'] = ''
        self.fields['cor'].widget.attrs['placeholder'] = 'Cor'

        self.fields['placa'].widget.attrs['class'] = ''
        self.fields['placa'].widget.attrs['placeholder'] = 'Placa'

