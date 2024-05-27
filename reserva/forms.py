from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nomeDoPet',
            'nomeDoDono',
            'telefone',
            'dia',
            'observacoes',
            'tamanho',
            'turno'
            ]
        widgets = {
            'dia' : forms.DateInput(attrs={'type': 'date', 'min': date.today()})
        }

    def clean_dia(self):
        dia = self.cleaned_data['dia']
        hoje = date.today()

        if dia < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para uma data do passado!')
        
        quantidade_de_reservas = Reserva.objects.filter(dia=dia).count()
        
        if quantidade_de_reservas >= 4:
            raise forms.ValidationError('A quantidade máxima de reserva para este data já foi antigida. Seliciona outra data.')
        
        return dia