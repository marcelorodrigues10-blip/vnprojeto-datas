from datetime import date
from datas import calcular_idade, dias_para_futuro
import pytest


def test_calcular_idade_aniversario_ja_passou():
    nascimento = date(1990, 5, 10)
    hoje = date(2026, 11, 11)
    assert calcular_idade(nascimento, hoje) == 36


def test_calcular_idade_aniversario_nao_passou():
    nascimento = date(1990, 12, 25)
    hoje = date(2026, 11, 11)
    assert calcular_idade(nascimento, hoje) == 35


def test_calcular_idade_data_futura_erro():
    nascimento = date(2030, 1, 1)
    hoje = date(2026, 11, 11)
    with pytest.raises(ValueError):
        calcular_idade(nascimento, hoje)


def test_dias_para_futuro():
    futuro = date(2026, 11, 21)
    hoje = date(2026, 11, 11)
    assert dias_para_futuro(futuro, hoje) == 10


def test_dias_para_futuro_data_passada_erro():
    passado = date(2020, 1, 1)
    hoje = date(2026, 11, 11)
    with pytest.raises(ValueError):
        dias_para_futuro(passado, hoje)



# Atualize a linha de importação no topo:
from datas import calcular_idade, dias_desde_passado, dias_para_futuro


# Adicione ao final do arquivo:
def test_dias_desde_passado():
    passado = date(2026, 11, 1)
    hoje = date(2026, 11, 11)
    assert dias_desde_passado(passado, hoje) == 10


def test_dias_desde_passado_data_futura_erro():
    futuro = date(2030, 1, 1)
    hoje = date(2026, 11, 11)
    with pytest.raises(ValueError):
        dias_desde_passado(futuro, hoje)
