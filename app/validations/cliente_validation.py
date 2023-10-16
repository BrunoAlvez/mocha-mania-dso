import re

from app.enums.telefone_enum import TelefoneEnum
from app.helpers.sanitizar_dados import SanitizarDados


class ClienteValidation:
    @staticmethod
    def valida_cpf(cpf: str):
        cpf = SanitizarDados.sanitizar(cpf)
        if len(cpf) != 11 or cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            raise ValueError('CPF inválido.')

        soma: int = 0
        for i in range(10, 1, -1):
            soma += int(cpf[10 - i]) * i
        resto_divisao: int = soma % 11
        digito_verificador: int = int(cpf[9])
        if (resto_divisao < 2 and digito_verificador != 0) or (digito_verificador != (11 - resto_divisao)):
            raise ValueError('CPF inválido.')

    @staticmethod
    def valida_telefone(telefone: str):
        telefone = SanitizarDados.sanitizar(telefone)
        ddd: int = int(telefone[:2])
        if ddd not in TelefoneEnum.ddds():
            raise ValueError('DDD inválido.')
        elif len(telefone) != 11:
            raise ValueError('Número de telefone inválido.')
        elif int(telefone[2]) not in TelefoneEnum.digitos_adicionais():
            raise ValueError('Número de telefone inválido.')

    @staticmethod
    def valida_email(email: str):
        if not re.match(r'^[\w-]+@([\w-]+\.)+[\w-]+$', email):
            raise ValueError('E-mail inválido.')
