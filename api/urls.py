from api.views import ReservaModelViewSet, CategoriaAnimalModelViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter(trailing_slash=False) # Não adiciona a '/' no final da URL.
router.register('reserva', ReservaModelViewSet)
router.register('categoria_animal', CategoriaAnimalModelViewSet)

urlpatterns = []
urlpatterns += router.urls

