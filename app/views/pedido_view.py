from datetime import date

from app.views.view_base import ViewBase


class PedidoView(ViewBase):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def cadastrar(self):
        data = date.today()
        cliente = self.input_int('ID do Cliente: ')
        funcionario = self.input_int('ID do Funcionário: ')
        itens = []
        while True:
            produto = self.input_int('ID do produto (0 para parar): ')
            if produto == 0:
                break
            itens.append(produto)
        try:
            pedido = self.__controlador.store({
                'data': data,
                'cliente': cliente,
                'responsavel': funcionario,
                'itens': itens,
            })
            print(f'Pedido #{pedido.id} cadastrado com sucesso.')
        except ValueError as error:
            print(error)

    def buscar(self):
        pedidos = self.__controlador.index()
        if len(pedidos) == 0:
            print('Nenhum pedido cadastrado.')
        else:
            print('Lista de pedidos:')
            for pedido in pedidos:
                print(pedido)

    def visualizar(self):
        id = input('ID: ')
        pedido = self.__controlador.show(id)
        if pedido is None:
            print(f'Pedido #{id} não encontrado.')
        else:
            print(pedido)

    def escolher_funcao(self) -> int:
        print('Escolha uma opção:')
        print('1 - Cadastrar pedido')
        print('2 - Listar pedidos')
        print('3 - Buscar pedido')
        print('4 - Voltar')
        return self.input_int('Opção: ')
