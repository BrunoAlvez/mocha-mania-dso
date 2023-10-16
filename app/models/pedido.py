import datetime

from app.models.cliente import Cliente
from app.models.funcionario import Funcionario
from app.models.produto import Produto


class Pedido:
    def __init__(self, id: int, data: datetime.datetime, cliente: Cliente, responsavel: Funcionario, itens: [Produto]):
        self.__id = id
        self.__data = data
        self.__cliente = cliente
        self.__responsavel = responsavel
        self.__itens = itens

    @staticmethod
    def fillable() -> list:
        return ['data', 'cliente', 'responsavel', 'itens']

    @property
    def id(self) -> int:
        return self.__id

    @property
    def data(self) -> datetime.datetime:
        return self.__data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def responsavel(self) -> Funcionario:
        return self.__responsavel

    @property
    def itens(self) -> [Produto]:
        return self.__itens

    def data_formatada(self) -> str:
        return self.__data.strftime('%d/%m/%Y')

    def __str__(self):
        return f'Pedido #{self.id} de {self.cliente.nome} em {self.data_formatada}'
