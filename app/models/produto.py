class Produto:
    def __init__(self, id: int, nome: str, descricao: str, valor: float):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise TypeError('Valor deve ser um número!')
        self.__valor = valor

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Descrição: {self.descricao} - Valor: {self.valor}'
