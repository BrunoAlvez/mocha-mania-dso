from enum import Enum


class ClassificacaoEnum(Enum):
    BRONZE = 'BRONZE'
    PRATA = 'PRATA'
    OURO = 'OURO'
    DIAMANTE = 'DIAMANTE'

    @staticmethod
    def valores():
        return [classificacao.value for classificacao in ClassificacaoEnum]
