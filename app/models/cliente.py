from app.models.pessoa import Pessoa
from app.validations.cliente_validation import ClienteValidation
from app.helpers.sanitizar_dados import SanitizarDados


class Cliente(Pessoa):
    def __init__(self, id: int, nome: str, login: str, email: str, cpf: str, telefone: str):
        super().__init__(id, nome, login, email)

        ClienteValidation.valida_cpf(cpf)
        ClienteValidation.valida_telefone(telefone)

        self.__cpf = SanitizarDados.sanitizar(cpf)
        self.__telefone = SanitizarDados.sanitizar(telefone)
        self.__senha = None
        self.__fidelidade = None

    @staticmethod
    def fillable() -> list:
        return ['nome', 'login', 'email', 'cpf', 'telefone']

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        ClienteValidation.valida_cpf(cpf)
        self.__cpf = SanitizarDados.sanitizar(cpf)

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        ClienteValidation.valida_telefone(telefone)
        self.__telefone = SanitizarDados.sanitizar(telefone)

    @property
    def fidelidade(self) -> int:
        return self.__fidelidade

    @fidelidade.setter
    def fidelidade(self, fidelidade: int):
        if self.fidelidade is None:
            self.__fidelidade = fidelidade
        else:
            raise ValueError('Fidelidade já cadastrada.')

    def telefone_formatado(self) -> str:
        return f'({self.__telefone[:2]}) {self.__telefone[2:7]}-{self.__telefone[7:]}'

    def cpf_formatado(self) -> str:
        return f'{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}'

    def __str__(self) -> str:
        return f'ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf_formatado()}'
