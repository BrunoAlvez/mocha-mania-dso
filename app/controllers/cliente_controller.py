from app.models.cliente import Cliente
from app.models.fidelidade import Fidelidade
from app.validations.cliente_validation import ClienteValidation
from app.views.cliente_view import ClienteView


class ClienteController:
    def __init__(self):
        self.tela = ClienteView(self)
        self.__clientes: [Cliente] = []

    @property
    def clientes(self):
        return self.__clientes

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
            self.tela.excluir()
        elif opcao == 6:
            self.tela.fidelizar()
        elif opcao == 7:
            return False
        else:
            return None
        return True

    def index(self, filtro: str) -> list:
        if filtro == '':
            return self.clientes
        return [
            cliente for cliente in self.clientes
            if filtro.lower() in cliente.nome.lower()
        ]

    def store(self, dados: dict) -> Cliente:
        dados = self.__validar_dados(dados)
        cliente = Cliente(*dados)
        self.clientes.append(cliente)
        return cliente

    def show(self, id: int) -> Cliente or None:
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def update(self, id: int, dados: dict) -> Cliente or None:
        dados = self.__validar_dados(dados, id)
        for indice, cliente in enumerate(self.clientes):
            if cliente.id == id:
                cliente = Cliente(*dados)
                self.clientes[indice] = cliente
                return cliente
        return None

    def destroy(self, id: int) -> bool:
        for indice, cliente in enumerate(self.clientes):
            if cliente.id == id:
                del self.clientes[indice]
                return True
        return False

    def fidelizar(self, id: int) -> Cliente or None:
        cliente = self.show(id)
        if cliente is not None:
            cliente.fidelidade = Fidelidade()
        return cliente

    def __validar_dados(self, dados: dict, id: int = None) -> list:
        atributos = {
            'nome': 'Nome',
            'login': 'Login',
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone',
        }
        for fillable in Cliente.fillable():
            if fillable not in dados or dados.get(fillable) == '':
                raise ValueError(f'{atributos.get(fillable)} não informado.')
        for cliente in self.clientes:
            if cliente.cpf == dados.get('cpf') and cliente.id != id:
                raise ValueError('CPF já cadastrado.')
            if cliente.login == dados.get('login') and cliente.id != id:
                raise ValueError('Login já cadastrado.')
            if cliente.email == dados.get('email') and cliente.id != id:
                raise ValueError('E-mail já cadastrado.')
        ClienteValidation.valida_cpf(dados.get('cpf'))
        ClienteValidation.valida_telefone(dados.get('telefone'))
        ClienteValidation.valida_email(dados.get('email'))

        if id is None:
            id = self.clientes[-1].id + 1 if len(self.clientes) > 0 else 1
        return [
            id,
            dados.get('nome'),
            dados.get('login'),
            dados.get('email'),
            dados.get('cpf'),
            dados.get('telefone'),
        ]
