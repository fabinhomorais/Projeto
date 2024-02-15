from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def aula_sobre_django(request):
    return render(request, 'aula_sobre_django.html')
   
def contato(request):
    return render(request, 'contato.html')