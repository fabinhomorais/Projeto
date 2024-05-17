from django.contrib import admin
from base.models import Contato


# Register your models here.
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'email', 'mensagem']
    search_fields = ['id','nome', 'email']