from app.models.pessoa import Pessoa
from app.enums.cargo_enum import CargoEnum


class Funcionario(Pessoa):
    def __init__(self, id: int, nome: str, login: str, email: str, cargo: CargoEnum):
        super().__init__(id, nome, login, email)
        self.__cargo = cargo

    @staticmethod
    def fillable() -> list:
        return ['nome', 'login', 'email', 'cargo']

    @property
    def cargo(self) -> CargoEnum:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: CargoEnum):
        if not isinstance(cargo, CargoEnum):
            raise TypeError('Cargo deve ser uma instância de CargoEnum!')
        self.__cargo = cargo

    def __str__(self):
        return f'ID: {self.id} | Nome: {self.nome} | Cargo: {self.cargo.value}'
