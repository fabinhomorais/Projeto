from django import forms
from base.models import Contato, Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nomeDoPet', 'telefone', 'dia', 'observacoes']
        widgets = {
            'dia' : forms.DateInput(attrs={'type': 'date'})
        }