from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):

    def clean_data(self): # Método 'clean' para validação.
        data = self.cleaned_data['data'] # Método 'clean' para validação.
        hoje = date.today()
        consulta = Reserva.objects.filter(data=data).count()
        if data < hoje or consulta >= 4:
            raise forms.ValidationError('RESERVA INDISPONÍVEL PARA ESSA DATA!')
        return data
    
    class Meta:
        model = Reserva
        fields = [
            'nome', 
            'email', 
            'nome_pet', 
            'data', 
            'turno', 
            'categoria_animal', 
            'observacoes'
        ]