from abc import ABC


class Pessoa(ABC):
    def __init__(self, id: int, nome: str, login: str, email: str):
        super().__init__()

        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__email = email
        self.__senha = None

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
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def senha(self) -> int:
        return hash(self.__senha)

    @senha.setter
    def senha(self, senha: str):
        self.__senha = hash(senha)
