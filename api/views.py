from rest_framework.viewsets import ModelViewSet
from reserva.models import Reserva, CategoriaAnimal
from api.serializers import ReservaModelSerializer, CategoriaAnimalModelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

class ReservaModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self): # Outra forma de implementar permissões.
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]


class CategoriaAnimalModelViewSet(ModelViewSet):
    queryset = CategoriaAnimal.objects.all()
    serializer_class = CategoriaAnimalModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]