from django.contrib import admin, messages
from base.models import Contato

@admin.action(description='Marcar Formulário(s) como Lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulário(s) de Contato(s) marcardo(s) como lido!', messages.SUCCESS)


@admin.action(description='Marcar Formulário(s) como NÃO Lido')
def marcar_como_nao_lido(modeladmin, request, queryset):
    queryset.update(lido=False)
    modeladmin.message_user(request, 'Formulário(s) de Contato(s) marcardo(s) como NÃO lido!', messages.SUCCESS)

# Register your models here.
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'email', 'mensagem', 'lido']
    search_fields = ['id','nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]