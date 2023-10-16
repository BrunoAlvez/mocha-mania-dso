class Ingrediente:
    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome}'
