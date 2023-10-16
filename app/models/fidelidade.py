from app.models.cliente import Cliente
from app.enums.classificacao_enum import ClassificacaoEnum


class Fidelidade:
    def __init__(self):
        self.__pontos = 0
        self.__classificacao = ClassificacaoEnum.BRONZE

    @property
    def pontos(self) -> int:
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos: int):
        if not isinstance(pontos, int):
            raise TypeError('Pontos deve ser um número inteiro!')
        self.__pontos = pontos

    @property
    def classificacao(self) -> ClassificacaoEnum:
        return self.__classificacao

    @classificacao.setter
    def classificacao(self, classificacao: ClassificacaoEnum):
        if not isinstance(classificacao, ClassificacaoEnum):
            raise TypeError('Classificação deve ser uma instância de ClassificacaoEnum!')
        self.__classificacao = classificacao

    def __str__(self) -> str:
        return f'Pontos: {self.pontos} | Classificação: {self.classificacao.value}'
