from app.views.view_base import ViewBase


class ReceitaView(ViewBase):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def cadastrar(self):
        dados = {
            'tempo_conclusao': self.input_int(f'Informe o tempo de conclusão (minutos): '),
            'nome': input(f'Informe o nome do produto: '),
            'descricao': input(f'Informe a descrição do produto: '),
            'valor': self.input_float(f'Informe o valor do produto: '),
            'ingredientes': [],
            'quantidades': [],
        }
        while True:
            ingrediente = self.input_int(f'Informe o ID do ingrediente (0 para parar): ')
            if ingrediente == 0:
                break
            dados['ingredientes'].append(ingrediente)
            dados['quantidades'].append(self.input_int(f'Informe a quantidade: '))
        try:
            receita = self.__controlador.store(dados)
            print(f'Receita #{receita.id} cadastrada com sucesso.')
        except ValueError as e:
            print(e)

    def listar(self):
        receitas = self.__controlador.index()
        if len(receitas) == 0:
            print('Nenhuma receita cadastrada.')
        else:
            print('Lista de receitas:')
            for receita in receitas:
                print(receita)

    def buscar(self):
        id = self.input_int('Informe o ID da receita: ')
        receita = self.__controlador.show(id)
        if receita is None:
            print('Receita não encontrada.')
        else:
            print(receita)

    def editar(self):
        while True:
            id = self.input_int('Informe o ID da receita: ')
            if self.__controlador.show(id) is None:
                print('Receita não encontrado.')
            else:
                break
        dados = {
            'tempo_conclusao': self.input_int(f'Informe o tempo de conclusão (minutos): '),
            'preparos': [],
        }
        while True:
            preparo = self.input_int(f'Informe o ID do preparo: ')
            if preparo == 0:
                break
            dados['preparos'].append(preparo)
        try:
            receita = self.__controlador.update(id, dados)
            if receita is None:
                print('Receita não encontrada.')
            else:
                print(f'Receita #{receita.id} editada com sucesso.')
        except ValueError as e:
            print(e)

    def escolher_funcao(self) -> int:
        print('Escolha uma opção:')
        print('1 - Cadastrar receita')
        print('2 - Listar receitas')
        print('3 - Buscar receita')
        print('4 - Editar receita')
        print('5 - Voltar')
        return self.input_int('Opção: ')
