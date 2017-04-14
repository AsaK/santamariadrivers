from rest_framework import serializers
from base.models import Motorista


class MotoristaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Motorista
        depth = 1
        fields = ['nome','cpf','rg','celular','endereco','orgao_emissor','data_nascimento','cnh_numero','cnh_primeira','cnh_validade','cnh_categoria','motivo','marca','modelo','cor','placa','ano','status','usuario','foto','foto_carro']

