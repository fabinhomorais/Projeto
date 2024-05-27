from django.shortcuts import render
from reserva.forms import ReservaForm

# Create your views here.
def reserva(request):
    sucesso = False

    if request.method == 'GET':
        form = ReservaForm()
    elif request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()

    context = {
        'nome': 'Fabio Morais',
        'telefone': '81 99999-9999',
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'reserva_de_banho.html', context)