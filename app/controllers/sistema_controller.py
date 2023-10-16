from app.controllers.cliente_controller import ClienteController
from app.controllers.estoque_controller import EstoqueController
from app.controllers.funcionario_controller import FuncionarioController
from app.controllers.pedido_controller import PedidoController
from app.controllers.receita_controller import ReceitaController
from app.views.sistema_view import SistemaView


class SistemaController:
    def __init__(self):
        self.__controlador_cliente = ClienteController()
        self.__controlador_funcionario = FuncionarioController()
        self.__controlador_estoque = EstoqueController()
        self.__controlador_receita = ReceitaController(self.__controlador_estoque)
        self.__controlador_pedido = PedidoController(
            self.__controlador_cliente,
            self.__controlador_funcionario,
            self.__controlador_estoque,
            self.__controlador_receita,
        )
        self.tela = SistemaView(self)

    def menu(self, opcao: int) -> bool or None:
        if opcao == 1:
            self.__controlador_cliente.tela.menu()
        elif opcao == 2:
            self.__controlador_funcionario.tela.menu()
        elif opcao == 3:
            self.__controlador_estoque.tela.menu()
        elif opcao == 4:
            self.__controlador_receita.tela.menu()
        elif opcao == 5:
            self.__controlador_pedido.tela.menu()
        elif opcao == 6:
            return False
        else:
            return None
        return True
