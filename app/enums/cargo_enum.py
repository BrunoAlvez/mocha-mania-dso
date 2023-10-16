from enum import Enum


class CargoEnum(Enum):
    GERENTE = 'GERENTE'
    ATENDENTE = 'ATENDENTE'
    BARISTA = 'BARISTA'

    @staticmethod
    def valores():
        return [cargo.value for cargo in CargoEnum]
