from django.contrib import admin
from reserva.models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomeDoPet', 'nomeDoDono', 'dia', 'turno']
    search_fields = ['id', 'nomeDoPet', 'nomeDoDono']
    list_filter = ['dia', 'turno', 'tamanho']
    ordering = ['id'] #Colocar o formulário em ordem