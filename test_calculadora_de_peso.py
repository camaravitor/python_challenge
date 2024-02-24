# test_calculadora_de_peso.py

import pytest
from calculadora_de_peso import obter_peso_ideal

def test_peso_ideal_masculino():
    # Teste para sexo masculino
    altura = 1.75
    sexo = 'M'
    assert obter_peso_ideal(altura, sexo) == pytest.approx((72.7 * altura) - 58)

def test_peso_ideal_feminino():
    # Teste para sexo feminino
    altura = 1.65
    sexo = 'F'
    assert obter_peso_ideal(altura, sexo) == pytest.approx((62.1 * altura) - 44.7)

def test_altura_invalida():
    # Teste para altura fora do intervalo
    altura = 2.6
    sexo = 'M'
    with pytest.raises(ValueError):
        obter_peso_ideal(altura, sexo)

def test_sexo_invalido():
    # Teste para sexo inválido
    altura = 1.70
    sexo = 'X'
    with pytest.raises(ValueError):
        obter_peso_ideal(altura, sexo)
