from abc import ABC, abstractmethod

from app.validations.cliente_validation import ClienteValidation


class ViewBase(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def controlador(self):
        raise NotImplementedError

    def menu(self):
        while True:
            opcao = self.escolher_funcao()
            resposta_menu = self.controlador.menu(opcao)
            if resposta_menu is None:
                print('Opção inválida.')
            elif not resposta_menu:
                break
            print()

    @abstractmethod
    def escolher_funcao(self) -> int:
        raise NotImplementedError

    @staticmethod
    def input_int(mensagem: str) -> int:
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print('Valor inválido.')

    @staticmethod
    def input_float(mensagem: str) -> float:
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print('Valor inválido.')

    @staticmethod
    def input_cpf(mensagem: str) -> str:
        while True:
            try:
                valor = input(mensagem)
                ClienteValidation.valida_cpf(valor)
                return valor
            except ValueError as error:
                print(error)

    @staticmethod
    def input_telefone(mensagem: str) -> str:
        while True:
            try:
                valor = input(mensagem)
                ClienteValidation.valida_telefone(valor)
                return valor
            except ValueError as error:
                print(error)

    @staticmethod
    def input_email(mensagem: str) -> str:
        while True:
            try:
                valor = input(mensagem)
                ClienteValidation.valida_email(valor)
                return valor
            except ValueError as error:
                print(error)
