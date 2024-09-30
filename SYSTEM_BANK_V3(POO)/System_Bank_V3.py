from abc import ABC, abstractclassmethod, abstractproperty
import time


def intro():
    print("\t\nBEM VINDO AO SISTEMA BANCARIO")
    time.sleep(2)

def menu1():
    menu1 = """
     #####################################
     #                                   #
     #        [1]Acessar Conta           #
     #        [2]Novo usuário            #
     #        [3]Nova conta              #
     #        [4]Listar contas           #
     #        [q]Sair                    #
     #                                   #
     #####################################

    ->"""
    return input(menu1)


def menu2():
    menu2 = """
     #####################################
     #                                   #
     #        [1]Depositar               #
     #        [2]Sacar                   #
     #        [3]Extrato                 #
     #        [4]Solicitar Mais Saque    #
     #        [5]Voltar/Sair da Conta    #
     #                                   #
     #####################################

    ->"""
    return input(menu2)



# ========================          FUNÇÕES CONFORME MENU1          ===========================



def cadastro_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nUsuário Existente")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço => Logradouro, Numero - Complemento - Bairro - Cidade/Sigla Estado: ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n --- Cliente cadastrado com Sucesso --- ")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n\t\t --- CPF NÃO CADASTRADO --- ")
        print('''
              
            Importante:
            -Verifique se o CPF foi corretamente digitado.
            -Verifique se o CPF está cadastrado em um usuário válido.
            -Em caso de dúvidas entre em contato com o suporte do sistema bancario.
              
              ''')
        return

    print ("""   
        Agora você ira cadastrar uma senha numérica para acessar sua conta.
        Lembre-se de usar apenas NÚMEROS.
        Essa senha só poderá ser recuperada em contato com a central de atendimento.
        Lembre-se de guardar em local seguro, e não compartilhar com ninguém.
        Caso tenha alguma dúvida, entre em contato com a central de atendimento.
        """)
    time.sleep(2)

    conf_senha = None
    senha = 0

    while not conf_senha == senha:

        senha = input('inserir sua senha numérica:')
        conf_senha = input('confirme sua senha:')

        if not conf_senha == senha:
            print("senha não confere - Tentar novamente.")
        else:
            print("Senha cadastrada com sucesso.")
            break


    conta = ContaBanco.nova_conta(cliente=cliente, numero=numero_conta, senha=senha)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n --- Sua conta foi criada com sucesso! --- ")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None



def lista_de_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))



# ================                FUNÇÕES PARA O MENU 2                 ======================



def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n ---   Cliente não possui conta!   --- ")
        return None

    print("\nContas disponíveis:")
    for i, conta in enumerate(cliente.contas):
        print(f"[{i + 1}] Conta {conta.numero} - Agência {conta.agencia}")

    opcao = int(input("\nEscolha o número da conta: ")) - 1

    if opcao < 0 or opcao >= len(cliente.contas):
        print("\n ---   Opção inválida!   --- ")
        return None

    return cliente.contas[opcao] 

def validar_senha(conta):
    tentativas = 3
    while tentativas > 0:
        senha = input('Inserir sua senha numérica: ')
        if senha == conta.senha:
            print(" ---   Senha válida!   --- ")
            print("Acesando...")
            time.sleep(1)
            return True
        tentativas -= 1
        print(f"\nSenha não confere. Tentativas restantes: {tentativas}")
    print("\n\n\n ---   Número máximo de tentativas atingido. Acesso bloqueado.   --- ")
    return False


def depositar(cliente, conta):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("Valor inválido! Informe um número.")
        return
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)


def sacar(cliente, conta):
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print(" ---   Valor inválido! Informe um número.   --- ")
        return
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(cliente):
    if not cliente:
        print("\n ---   Cliente não encontrado!   --- ")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def solicitar_mais_saques(cliente):
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    if validar_senha(conta):  # Só permite solicitar mais saques se a senha for válida
        conta.solicitar_aumento_saque()



# ================         CLASSES PARA ORGANIZAÇÃO DE FUNÇÕES           ======================



class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, senha):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._senha = senha

    @classmethod
    def nova_conta(cls, cliente, numero, senha):
        return cls(numero, cliente, senha)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @property
    def senha(self):
        return self._senha

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n --- Operação falhou! Você não tem saldo suficiente.   --- ")
        elif valor > 0:
            self._saldo -= valor
            print(f"\n\t ---   Saque no valor de R${valor} realizado   --- ")
            return True
        else:
            print("\n ---   Valor inválido.   ---  ")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n\t ---   Depósito no valor de R${valor} realizado.   --- ")
        else:
            print("\n ---   O valor informado é inválido.   --- ")
            return False

        return True


class ContaBanco(Conta):
    def __init__(self, numero, cliente, senha, limite=500, limite_saques=3, solicitacao_limite_saque=0):
        super().__init__(numero, cliente, senha)
        self._limite = limite
        self._limite_saques = limite_saques
        self.solicitacao_limite_saque = solicitacao_limite_saque  # Contador de solicitações de saque

    def solicitar_aumento_saque(self):
        if self.solicitacao_limite_saque >= 1:  # Exemplo: Limitar a uma solicitação por dia
            print("\n --- Você já fez uma solicitação de aumento hoje! Tente novamente amanhã. ---")
        else:
            self._limite_saques += 1
            self.solicitacao_limite_saque += 1
            print(f"\n --- Solicitação de aumento de limite de saques aprovada! Novo limite: {self._limite_saques} saques diários. ---")

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n --- O valor selecionado é superior ao limite por saque (R$ 500,00). --- ")
        elif excedeu_saques:
            print("\n --- Para sua segurança, esta operação está bloqueada --- ")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)




# ===================================    EXECUÇÃO DO PROGRAMA   =================================



def program():
    clientes = []
    contas = []

    while True:
        opcao = menu1()
        if opcao == "1":  # acessar conta - necessário cpf cadastrado e possuir pelo menos 1 numero de conta
            while True:
                cpf = input("Informe o CPF do cliente: (ou Digite 'q' para voltar)")
                if cpf.lower() == 'q':
                    break
                cliente = filtrar_cliente(cpf, clientes)
                if not cliente:
                    print(' --- CPF de usuário não encontrado - Tente Novamente --- ')
                else:
                    conta_selecionada = recuperar_conta_cliente(cliente)
                    if conta_selecionada and validar_senha(conta_selecionada):
                        while True:
                            opcao = menu2()
                            if opcao == "1":
                                depositar(cliente, conta_selecionada)
                            elif opcao == "2":
                                sacar(cliente, conta_selecionada)
                            elif opcao == "3":
                                exibir_extrato(cliente)
                            elif opcao == "4":
                                solicitar_mais_saques(cliente)
                            elif opcao == "5":
                                break
                            else:
                                print("\nOperação inválida! Selecionar opção Válida.")
                        break

        elif opcao == "2":
            cadastro_cliente(clientes)

        elif opcao == "3":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "4":
            lista_de_contas(contas)

        elif opcao.lower() == "q":
            break

        else:
            print("\nOperação inválida! Selecionar opção Válida.")


# ===================================    CHAMAMENTO DO PROGRAMA   =================================


intro()
program()