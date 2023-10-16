from app.enums.cargo_enum import CargoEnum
from app.models.funcionario import Funcionario
from app.views.funcionario_view import FuncionarioView


class FuncionariosController:
    def __init__(self):
        self.tela = FuncionarioView(self)
        self.__funcionarios: [Funcionario] = []

    @property
    def funcionarios(self):
        return self.__funcionarios

    def menu(self, opcao: int) -> bool or None:
        if opcao == 1:
            self.tela.cadastrar()
        elif opcao == 2:
            self.tela.listar()
        elif opcao == 3:
            self.tela.buscar()
        elif opcao == 4:
            self.tela.editar()
        elif opcao == 5:
            self.tela.excluir()
        elif opcao == 6:
            return False
        else:
            return None
        return True

    def index(self):
        return self.funcionarios

    def store(self, dados: dict):
        dados = self.__validar_dados(dados)
        funcionario = Funcionario(*dados)
        self.funcionarios.append(funcionario)
        return funcionario

    def show(self, id: int):
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                return funcionario
        return None

    def update(self, id: int, dados: dict) -> Funcionario or None:
        dados = self.__validar_dados(dados, id)
        for indice, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                funcionario = Funcionario(*dados)
                self.funcionarios[indice] = funcionario
                return funcionario
        return None

    def destroy(self, id: int):
        for indice, funcionario in enumerate(self.funcionarios):
            if funcionario.id == id:
                del self.funcionarios[indice]
                return True
        return False

    def __validar_dados(self, dados: dict, id: int = None) -> list:
        atributos = {
            'nome': 'Nome',
            'login': 'Login',
            'email': 'E-mail',
            'cargo': 'Cargo',
        }
        for fillable in Funcionario.fillable():
            if fillable not in dados or dados.get(fillable) == '':
                raise ValueError(f'{atributos[fillable]} não informado.')
        if id is None:
            id = self.funcionarios[-1].id + 1 if len(self.funcionarios) > 0 else 1
        return [
            id,
            dados.get('nome'),
            dados.get('login'),
            dados.get('email'),
            self.traduz_cargo(dados.get('cargo')),
        ]

    @staticmethod
    def traduz_cargo(cargo: int) -> CargoEnum:
        if cargo == 1:
            return CargoEnum.GERENTE
        elif cargo == 2:
            return CargoEnum.ATENDENTE
        elif cargo == 3:
            return CargoEnum.BARISTA
        else:
            raise ValueError('Cargo inválido.')
