from app.controllers.estoque_controller import EstoqueController
from app.models.preparo import Preparo
from app.models.produto import Produto
from app.models.receita import Receita
from app.views.receita_view import ReceitaView


class ReceitaController:
    def __init__(self, controlador_estoques: EstoqueController):
        self.tela = ReceitaView(self)
        self.__receitas = []
        self.__preparos = []
        self.__produtos = []
        self.__controlador_estoques = controlador_estoques

    @property
    def receitas(self) -> [Receita]:
        return self.__receitas

    @property
    def preparos(self) -> [Preparo]:
        return self.__preparos

    @property
    def produtos(self) -> [Produto]:
        return self.__produtos

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

    def index(self):
        return self.receitas

    def store(self, dados: dict):
        dados = self.__validar_dados(dados)
        receita = Receita(*dados)
        self.receitas.append(receita)
        return receita

    def show(self, id: int):
        for receita in self.receitas:
            if receita.id == id:
                return receita
        return None

    def update(self, id: int, dados: dict) -> Receita or None:
        dados = self.__validar_dados(dados)
        for indice, cliente in enumerate(self.receitas):
            if cliente.id == id:
                self.receitas[indice] = Receita(*dados)
                return cliente
        return None

    def __validar_dados(self, dados: dict) -> list:
        atributos = {
            'tempo_conclusao': 'Tempo de conclusão',
            'nome': 'Nome do produto',
            'descricao': 'Descricao do produto',
            'valor': 'Valor do produto',
            'ingredientes': 'Ingredientes',
            'quantidades': 'Quantidades',
        }
        for fillable in Receita.fillable():
            if fillable not in dados:
                raise KeyError(f'{atributos[fillable]} não foi informado.')
        if not isinstance(dados['tempo_conclusao'], (float, int)):
            raise TypeError('O tempo de conclusão deve ser um número.')
        elif dados['tempo_conclusao'] < 0:
            raise ValueError('O tempo de conclusão não pode ser negativo.')
        if dados.get('ingredientes') is None:
            raise ValueError('Nenhum ingrediente informado.')
        ids_ingrediente_cadastrados = [ingrediente.id for ingrediente in self.__controlador_estoques.ingredientes]
        for ingrediente in dados.get('ingredientes'):
            if ingrediente not in ids_ingrediente_cadastrados:
                raise ValueError(f'Ingrediente #{ingrediente} não cadastrado.')
        preparos_selecionados = []
        for indice, ingrediente in enumerate(dados.get('ingredientes')):
            if dados.get('quantidades')[indice] < 0:
                raise ValueError(f'Quantidade do ingrediente #{ingrediente} não pode ser negativa.')
            for estoque in self.__controlador_estoques.estoques:
                if estoque.ingrediente is not None and estoque.ingrediente.id == ingrediente:
                    if estoque.quantidade < dados.get('quantidades')[indice]:
                        raise ValueError(
                            f'Quantidade do ingrediente #{ingrediente} não pode ser maior que a quantidade em estoque.'
                        )
            for ingrediente_estocado in self.__controlador_estoques.ingredientes:
                if ingrediente_estocado.id == ingrediente:
                    ingrediente = ingrediente_estocado
            preparo = Preparo(
                id=len(self.__preparos) + 1,
                ingrediente=ingrediente,
                quantidade=dados.get('quantidades')[indice],
            )
            self.__preparos.append(preparo)
            preparos_selecionados.append(preparo)
        return [
            self.receitas[-1].id + 1 if len(self.receitas) > 0 else 1,
            dados['tempo_conclusao'] * 60,
            self.__cadastra_produto(dados),
            preparos_selecionados,
        ]

    def __cadastra_produto(self, dados: dict) -> Produto:
        if 'nome' not in dados or dados.get('nome') == '':
            raise ValueError('Nome do produto não informado.')
        if 'descricao' not in dados or dados.get('descricao') == '':
            raise ValueError('Descrição do produto não informada.')
        if 'valor' not in dados or dados.get('valor') == '':
            raise ValueError('Valor do produto não informado.')
        if dados.get('valor') < 0:
            raise ValueError('Valor do produto não pode ser negativo.')
        if dados.get('nome') in [produto.nome for produto in self.__produtos]:
            raise ValueError('Produto já cadastrado.')
        if not isinstance(dados.get('valor'), (float, int)):
            raise TypeError('Valor do produto deve ser um número.')
        produto = Produto(
            id=len(self.__produtos) + 1,
            nome=dados.get('nome'),
            descricao=dados.get('descricao'),
            valor=float(dados.get('valor')),
        )
        self.__produtos.append(produto)
        return produto
