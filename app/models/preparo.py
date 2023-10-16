from app.models.ingrediente import Ingrediente


class Preparo:
    def __init__(self, id: int, quantidade: float, ingrediente: Ingrediente):
        self.__id = id
        self.__quantidade = quantidade
        self.__ingrediente = ingrediente

    @property
    def id(self) -> int:
        return self.__id

    @property
    def quantidade(self) -> float:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: float):
        if not isinstance(quantidade, float):
            raise TypeError('A quantidade deve ser um float.')
        elif quantidade < 0:
            raise ValueError('A quantidade não pode ser negativa.')
        self.__quantidade = quantidade

    @property
    def ingrediente(self) -> Ingrediente:
        return self.__ingrediente
