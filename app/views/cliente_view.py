from app.views.view_base import ViewBase


class ClienteView(ViewBase):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    def cadastrar(self):
        dados = {
            'nome': input(f'Informe o nome: '),
            'login': input(f'Informe o login: '),
            'email': self.input_email(f'Informe o e-mail: '),
            'cpf': self.input_cpf(f'Informe o CPF: '),
            'telefone': self.input_telefone(f'Informe o telefone: '),
        }
        try:
            cliente = self.__controlador.store(dados)
            print(f'Cliente {cliente.nome} cadastrado com sucesso.')
        except ValueError as e:
            print(e)

    def buscar(self):
        filtro = input('Informe o nome do cliente: ')
        clientes = self.__controlador.index(filtro)
        if len(clientes) == 0:
            print('Nenhum cliente cadastrado.')
        else:
            print('Lista de clientes:')
            for cliente in clientes:
                print(cliente)

    def visualizar(self):
        id = self.input_int('Informe o ID do cliente: ')
        cliente = self.__controlador.show(id)
        if cliente is None:
            print('Cliente não encontrado.')
        else:
            print(cliente)

    def editar(self):
        while True:
            id = self.input_int('Informe o ID do cliente: ')
            if self.__controlador.show(id) is None:
                print('Cliente não encontrado.')
            else:
                break
        dados = {
            'nome': input(f'Informe o nome: '),
            'login': input(f'Informe o login: '),
            'email': self.input_email(f'Informe o e-mail: '),
            'cpf': self.input_cpf(f'Informe o CPF: '),
            'telefone': self.input_telefone(f'Informe o telefone: '),
        }
        try:
            cliente = self.__controlador.update(id, dados)
            if cliente is None:
                print('Cliente não encontrado.')
            else:
                print(f'Cliente {cliente.nome} editado com sucesso.')
        except ValueError as e:
            print(e)

    def excluir(self):
        id = self.input_int('Informe o ID do cliente: ')
        if self.__controlador.destroy(id):
            print('Cliente excluído com sucesso.')
        else:
            print('Cliente não encontrado.')

    def fidelizar(self):
        id = self.input_int('Informe o ID do cliente: ')
        cliente = self.__controlador.fidelizar(id)
        if cliente is None:
            print('Cliente não encontrado.')
        else:
            print(f'Cliente {cliente.nome} fidelizado com sucesso.')

    def escolher_funcao(self) -> int:
        print('1 - Cadastrar cliente')
        print('2 - Listar clientes')
        print('3 - Buscar cliente')
        print('4 - Editar cliente')
        print('5 - Excluir cliente')
        print('6 - Fidelizar cliente')
        print('7 - Voltar')
        return self.input_int('Escolha uma função: ')
