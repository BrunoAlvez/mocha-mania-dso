from app.models.ingrediente import Ingrediente


class Estoque:
    def __init__(self, id: int, quantidade: float, item: Ingrediente = None):
        self.__id = id
        self.__quantidade = quantidade
        if isinstance(item, Ingrediente):
            self.__ingrediente = item
        else:
            raise TypeError('Item deve ser uma instância de Ingrediente!')

    @staticmethod
    def fillable() -> list:
        return ['quantidade', 'item']

    @property
    def id(self) -> int:
        return self.__id

    @property
    def quantidade(self) -> float:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: float):
        if not isinstance(quantidade, (int, float)):
            raise TypeError('Quantidade deve ser um número!')
        self.__quantidade = quantidade

    @property
    def ingrediente(self) -> Ingrediente:
        return self.__ingrediente

    @ingrediente.setter
    def ingrediente(self, ingrediente: Ingrediente):
        if not isinstance(ingrediente, Ingrediente):
            raise TypeError('Ingrediente deve ser uma instância de Ingrediente!')
        self.__ingrediente = ingrediente

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Quantidade: {self.quantidade}\n' \
               f'Item: {self.ingrediente}'
