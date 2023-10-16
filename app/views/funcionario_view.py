from app.views.view_base import ViewBase


class FuncionarioView(ViewBase):
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
            'email': input(f'Informe o e-mail: '),
            'cargo': self.input_int(f'Informe o cargo (1 - Gerente, 2 - Atendente, 3 - Barista): '),
        }
        try:
            funcionario = self.__controlador.store(dados)
            print(f'Funcionario {funcionario.nome} cadastrado com sucesso.')
        except ValueError as e:
            print(e)

    def buscar(self):
        filtro = input('Informe o nome do funcionario: ')
        funcionarios = self.__controlador.index(filtro)
        if len(funcionarios) == 0:
            print('Nenhum funcionario cadastrado.')
        else:
            print('Lista de funcionarios:')
            for funcionario in funcionarios:
                print(funcionario)

    def visualizar(self):
        id = self.input_int('Informe o ID do funcionario: ')
        funcionario = self.__controlador.show(id)
        if funcionario is None:
            print('Funcionario não encontrado.')
        else:
            print(funcionario)

    def editar(self):
        while True:
            id = self.input_int('Informe o ID do funcionário: ')
            if self.__controlador.show(id) is None:
                print('Funcionário não encontrado.')
            else:
                break
        dados = {
            'nome': input(f'Informe o nome: '),
            'login': input(f'Informe o login: '),
            'email': input(f'Informe o e-mail: '),
            'cargo': self.input_int(f'Informe o cargo (1 - Gerente, 2 - Atendente, 3 - Barista): '),
        }
        try:
            funcionario = self.__controlador.update(id, dados)
            if funcionario is None:
                print('Funcionario não encontrado.')
            else:
                print(f'Funcionario {funcionario.nome} editado com sucesso.')
        except ValueError as e:
            print(e)

    def excluir(self):
        id = self.input_int('Informe o ID do funcionario: ')
        if self.__controlador.destroy(id):
            print(f'Funcionario excluído com sucesso.')
        else:
            print('Funcionario não encontrado.')

    def escolher_funcao(self) -> int:
        print('Gerenciamento de Funcionarios')
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Buscar')
        print('4 - Editar')
        print('5 - Excluir')
        print('6 - Voltar')
        return self.input_int('Escolha uma opção: ')
