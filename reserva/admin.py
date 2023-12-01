from django.contrib import admin # Admin também é uma App do Django.
from reserva.models import Reserva, CategoriaAnimal


@admin.register(CategoriaAnimal)
class CategoriaAnimalAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.action(description='Banho(s) Concluído(s)')
def marcar_banho_concluido(modeladmin, request, queryset):
    queryset.update(banho_conclusao=True)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data', 'turno', 'banho_conclusao']
    search_fields = ['nome', 'email', 'nome_pet', 'categoria_animal__nome', 'data']
    list_filter = ['banho_conclusao', 'data', 'turno', 'categoria_animal']
    actions = [marcar_banho_concluido]