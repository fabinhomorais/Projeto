import pytest
from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta
from reserva.models import Reserva

def test_reserva_view_deve_retornar_template_correto(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva_de_banho.html')


@pytest.fixture
def reserva_valida():
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nomeDoPet': 'Lua',
        'nomeDoDono': 'Fabio',
        'telefone': '81 999999999',
        'dia': amanha,
        'observacoes': 'Lua fica muito agitada quando toma banho',
        'tamanho': 0,
        'turno': 'tarde'
    }
    return dados

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, reserva_valida):
    response = client.post('/reserva/criar/', reserva_valida)

    assert response.status_code == 200
    assert 'Agendamento feito com sucesso' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva_no_banco(client, reserva_valida):
    response = client.post('/reserva/criar/', reserva_valida)

    assert response.status_code == 200
    assert 'Agendamento feito com sucesso' in str(response.content)

    assert Reserva.objects.all().count() == 1

    reserva = Reserva.objects.first()

    assert reserva.nomeDoPet == reserva_valida['nomeDoPet']