from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from reserva.models import Reserva, CategoriaAnimal

class CategoriaAnimalReservaNestedSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            'id',
            'nome',
            'email',
            'nome_pet',
            'data',
            'turno',
            'observacoes',
            'banho_conclusao',
        ]

class PrimaryKeyReservaField(PrimaryKeyRelatedField):
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        serializer = ReservaModelSerializer(instance=value)
        return serializer.data

class ReservaModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        '''fields = [
            'id',
            'nome',
            'email',
            'nome_pet',
            'data',
            'turno',
            'categoria_animal',
            'observacoes',
            'banho_conclusao'
        ]'''
        fields = '__all__'


class CategoriaAnimalModelSerializer(ModelSerializer):

    reservas_da_categoria = CategoriaAnimalReservaNestedSerializer(many=True)

    class Meta:
        model = CategoriaAnimal
        fields = [
            'id',
            'nome',
            'reservas_da_categoria',
        ]

class ReservaCategoriaAnimalSerializer(ModelSerializer):

    categoria_animal = PrimaryKeyReservaField(queryset=Reserva.objects.all())

    class Meta:
        model = Reserva
        fields = [
            'id',
            'nome',
            'email',
            'nome_pet',
            'data',
            'turno',
            'categoria_animal',
            'observacoes',
            'banho_conclusao'
        ]





