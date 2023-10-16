from app.views.cliente_view import ClienteView
from app.views.view_base import ViewBase


class SistemaView(ViewBase):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def escolher_funcao(self) -> int:
        print('Escolha uma opção:')
        print('1 - Clientes')
        print('2 - Funcionários')
        print('3 - Estoques')
        print('4 - Receitas')
        print('5 - Pedidos')
        print('6 - Sair')
        return self.input_int('Opção: ')
