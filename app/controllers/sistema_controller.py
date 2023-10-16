from app.controllers.clientes_controller import ClientesController
from app.controllers.estoques_controller import EstoquesController
from app.controllers.funcionarios_controller import FuncionariosController
from app.controllers.pedidos_controller import PedidosController
from app.controllers.receitas_controller import ReceitasController
from app.views.sistema_view import SistemaView


class SistemaController:
    def __init__(self):
        self.__controlador_clientes = ClientesController()
        self.__controlador_funcionarios = FuncionariosController()
        self.__controlador_estoques = EstoquesController()
        self.__controlador_receitas = ReceitasController(self.__controlador_estoques)
        self.__controlador_pedidos = PedidosController(
            self.__controlador_clientes,
            self.__controlador_funcionarios,
            self.__controlador_estoques,
            self.__controlador_receitas,
        )
        self.tela = SistemaView(self)

    def menu(self, opcao: int) -> bool or None:
        if opcao == 1:
            self.__controlador_clientes.tela.menu()
        elif opcao == 2:
            self.__controlador_funcionarios.tela.menu()
        elif opcao == 3:
            self.__controlador_estoques.tela.menu()
        elif opcao == 4:
            self.__controlador_receitas.tela.menu()
        elif opcao == 5:
            self.__controlador_pedidos.tela.menu()
        elif opcao == 6:
            return False
        else:
            return None
        return True
