from datetime import date


def calcular_idade(data_nascimento: date, data_referencia: date = None) -> int:
    """Calcula a idade em anos completos a partir da data de nascimento."""
    if data_referencia is None:
        data_referencia = date.today()

    if data_nascimento > data_referencia:
        raise ValueError("A data de nascimento não pode ser no futuro.")

    idade = data_referencia.year - data_nascimento.year
    # Ajusta caso o aniversário ainda não tenha ocorrido no ano de referência
    if (data_referencia.month, data_referencia.day) < (
        data_nascimento.month,
        data_nascimento.day,
    ):
        idade -= 1

    return idade


def dias_para_futuro(data_futura: date, data_referencia: date = None) -> int:
    """Calcula quantos dias faltam para uma data no futuro."""
    if data_referencia is None:
        data_referencia = date.today()

    if data_futura < data_referencia:
        raise ValueError("A data informada deve estar no futuro.")

    return (data_futura - data_referencia).days
