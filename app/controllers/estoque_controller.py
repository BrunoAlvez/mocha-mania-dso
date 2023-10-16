from app.models.estoque import Estoque
from app.models.ingrediente import Ingrediente
from app.views.estoque_view import EstoqueView


class EstoqueController:
    def __init__(self):
        self.tela = EstoqueView(self)
        self.__estoques = []
        self.__ingredientes = []

    @property
    def estoques(self):
        return self.__estoques

    @property
    def ingredientes(self):
        return self.__ingredientes

    def index(self):
        return self.estoques

    def menu(self, opcao: int) -> bool or None:
        if opcao == 1:
            self.tela.cadastrar()
        elif opcao == 2:
            self.tela.buscar()
        elif opcao == 3:
            self.tela.visualizar()
        elif opcao == 4:
            self.tela.editar()
        elif opcao == 5:
            return False
        else:
            return None
        return True

    def store(self, dados: dict) -> Estoque:
        dados = self.__validar_dados(dados)
        estoque = Estoque(*dados)
        self.estoques.append(estoque)
        return estoque

    def show(self, id: int) -> Estoque or None:
        for estoque in self.estoques:
            if estoque.id == id:
                return estoque
        return None

    def update(self, id: int, dados: dict) -> Estoque or None:
        estoque = self.show(id)
        if estoque is None:
            return None
        if 'quantidade' not in dados or dados.get('quantidade') is '':
            raise ValueError(f'Quantidade não informada.')
        if dados.get('quantidade') < 1:
            raise ValueError(f'Quantidade inválida.')
        estoque.quantidade = dados.get('quantidade')
        return estoque

    def __validar_dados(self, dados: dict) -> list:
        atributos = {
            'nome': 'Nome do item',
            'quantidade': 'Quantidade',
        }

        if 'nome' not in dados or dados.get('nome') is '':
            raise ValueError(f'{atributos["nome"]} não informado.')
        if 'quantidade' not in dados or dados.get('quantidade') is '':
            raise ValueError(f'{atributos["quantidade"]} não informado.')

        ingrediente = Ingrediente(
            self.ingredientes[-1].id + 1 if len(self.ingredientes) > 0 else 1,
            dados.get('nome'),
        )
        self.ingredientes.append(ingrediente)

        if dados.get('quantidade') < 1:
            raise ValueError(f'Quantidade inválida.')
        return [
            self.estoques[-1].id + 1 if len(self.estoques) > 0 else 1,
            dados.get('quantidade'),
            ingrediente,
        ]
