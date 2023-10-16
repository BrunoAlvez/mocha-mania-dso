from app.views.view_base import ViewBase


class EstoqueView(ViewBase):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def cadastrar(self):
        dados = {
            'nome': input(f'Informe o nome do ingrediente: '),
            'quantidade': self.input_int(f'Informe a quantidade: '),
        }
        try:
            estoque = self.__controlador.store(dados)
            print(f'Ingrediente {estoque.ingrediente.nome} cadastrado com sucesso.')
        except ValueError as e:
            print(e)

    def listar(self):
        estoques = self.__controlador.index()
        if len(estoques) == 0:
            print('Nenhum estoque cadastrado.')
        else:
            print('Lista de estoques:')
            for estoque in estoques:
                print(estoque)

    def buscar(self):
        id = self.input_int('Informe o ID do estoque: ')
        estoque = self.__controlador.show(id)
        if estoque is None:
            print('Estoque não encontrado.')
        else:
            print(estoque)

    def editar(self):
        while True:
            id = self.input_int('Informe o ID do estoque: ')
            if self.__controlador.show(id) is None:
                print('Estoque não encontrado.')
            else:
                break
        dados = {
            'quantidade': self.input_int(f'Informe a quantidade: '),
        }
        try:
            estoque = self.__controlador.update(id, dados)
            if estoque is None:
                print('Estoque não encontrado.')
            else:
                print(f'Estoque {estoque.item().nome} editado com sucesso.')
        except ValueError as e:
            print(e)

    def escolher_funcao(self) -> int:
        print('1 - Cadastrar estoque')
        print('2 - Listar estoques')
        print('3 - Buscar estoque')
        print('4 - Editar quantidade do estoque')
        print('5 - Voltar')
        return self.input_int('Escolha uma função: ')
