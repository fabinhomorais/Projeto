import pytest
from reserva.models import Reserva, Petshop
from model_bakery import baker
from datetime import date

def test_config():
    assert 1 == 1

@pytest.fixture
def reserva():
    dia = date(2024, 5, 29)
    reserva = baker.make(
        Reserva,
        nomeDoPet = 'Budy',
        dia = dia,
        turno = 'manha'
    )

    return reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Nome do Pet: Budy - Dia da reserva: 2024-05-29 - Turno: manha'


@pytest.mark.django_db
def test_qtd_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 5
    baker.make(
        Reserva,
        quantidade,
        petshop = petshop
    )


    assert petshop.qtd_reservas() == 5