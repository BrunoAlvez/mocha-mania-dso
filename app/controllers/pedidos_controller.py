from app.controllers.clientes_controller import ClientesController
from app.controllers.estoques_controller import EstoquesController
from app.controllers.funcionarios_controller import FuncionariosController
from app.controllers.receitas_controller import ReceitasController
from app.models.pedido import Pedido
from app.models.produto import Produto
from app.views.pedido_view import PedidoView


class PedidosController:
    def __init__(
        self,
        controlador_clientes: ClientesController,
        controlador_funcionarios: FuncionariosController,
        controlador_estoques: EstoquesController,
        controlador_receitas: ReceitasController,
    ):
        self.tela = PedidoView(self)
        self.__pedidos = []
        self.__controlador_clientes = controlador_clientes
        self.__controlador_funcionarios = controlador_funcionarios
        self.__controlador_estoques = controlador_estoques
        self.__controlador_receitas = controlador_receitas

    @property
    def pedidos(self):
        return self.__pedidos

    def menu(self, opcao: int) -> bool or None:
        if opcao == 1:
            self.tela.cadastrar()
        elif opcao == 2:
            self.tela.listar()
        elif opcao == 3:
            self.tela.buscar()
        elif opcao == 4:
            return False
        else:
            return None
        return True
    
    def index(self):
        return self.pedidos
    
    def store(self, dados: dict):
        dados = self.__validar_dados(dados)
        pedido = Pedido(*dados)
        self.pedidos.append(pedido)
        return pedido

    def show(self, id: int):
        for pedido in self.pedidos:
            if pedido.id == id:
                return pedido
        return None
    
    def __validar_dados(self, dados: dict) -> list:
        atributos = {
            'data': 'Data',
            'cliente': 'Cliente',
            'responsavel': 'Responsável',
            'itens': 'Itens',
        }
        for fillable in Pedido.fillable():
            if fillable not in dados or dados.get(fillable) == '':
                raise ValueError(f'{atributos[fillable]} não informado.')
        produtos_selecionados = self.produtos_selecionados(dados)
        cliente_selecionado = self.__controlador_clientes.show(dados.get('cliente'))
        if cliente_selecionado is None:
            raise ValueError(f'Cliente #{dados.get("cliente")} não cadastrado.')
        responsavel_selecionado = self.__controlador_funcionarios.show(dados.get('responsavel'))
        if responsavel_selecionado is None:
            raise ValueError(f'Responsável #{dados.get("responsavel")} não cadastrado.')
        self.modifica_estoque(produtos_selecionados)
        return [
            self.pedidos[-1].id + 1 if len(self.pedidos) > 0 else 1,
            dados.get('data'),
            cliente_selecionado,
            responsavel_selecionado,
            produtos_selecionados,
        ]

    def produtos_selecionados(self, dados: dict) -> [Produto]:
        ids_produtos_cadastrados = [produto.id for produto in self.__controlador_receitas.produtos]
        for produto in dados.get('itens'):
            if produto not in ids_produtos_cadastrados:
                raise ValueError(f'Produto #{produto} não cadastrado.')
        produtos_selecionados = []
        for produto in dados.get('itens'):
            for produto_cadastrado in self.__controlador_receitas.produtos:
                if produto == produto_cadastrado.id:
                    produtos_selecionados.append(produto_cadastrado)
        return produtos_selecionados

    def modifica_estoque(self, produtos_selecionados: [Produto]):
        receitas = self.__controlador_receitas.receitas
        ingredientes = self.__controlador_estoques.ingredientes
        for receita in receitas:
            for produto in produtos_selecionados:
                if produto.id == receita.produto.id:
                    for preparo in receita.preparos:
                        if preparo.ingrediente.id not in [ingrediente.id for ingrediente in ingredientes]:
                            raise ValueError(f'Ingrediente #{preparo.ingrediente.id} não cadastrado.')
                        for estoque in self.__controlador_estoques.estoques:
                            if estoque.ingrediente.id == preparo.ingrediente.id:
                                if estoque.quantidade < preparo.quantidade:
                                    raise ValueError(f'Quantidade insuficiente de {estoque.ingrediente.nome}.')
                                else:
                                    estoque.quantidade -= preparo.quantidade

