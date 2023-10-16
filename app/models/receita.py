from app.models.preparo import Preparo
from app.models.produto import Produto


class Receita:
    def __init__(self, id: int, tempo_conclusao: int, produto: Produto, preparos: [Preparo]):
        self.__id = id
        self.__tempo_conclusao = tempo_conclusao
        self.__produto = produto
        self.__preparos = preparos

    @staticmethod
    def fillable() -> list:
        return ['tempo_conclusao', 'nome', 'descricao', 'valor', 'ingredientes', 'quantidades']

    @property
    def id(self) -> int:
        return self.__id

    @property
    def tempo_conclusao(self) -> int:
        return self.__tempo_conclusao

    @tempo_conclusao.setter
    def tempo_conclusao(self, tempo_conclusao: int):
        if not isinstance(tempo_conclusao, int):
            raise TypeError('O tempo de conclusão deve ser um inteiro.')
        elif tempo_conclusao < 0:
            raise ValueError('O tempo de conclusão não pode ser negativo.')
        self.__tempo_conclusao = tempo_conclusao

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def preparos(self) -> [Preparo]:
        return self.__preparos

    def __str__(self):
        return f'ID: {self.id} | Tempo de conclusão: {self.tempo_conclusao} | Produto: {self.produto.nome}'

