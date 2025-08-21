from abc import ABC, abstractmethod
import textwrap
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, cpf, data_nascimento, endereco)

class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3
        self.historico = Historico()

    def sacar(self, saque):
        return saque.registrar(self)

    def depositar(self, deposito):
        return deposito.registrar(self)

    def exibir_extrato(self):
        self.historico.exibir(self.saldo)

class ContaCorrente(Conta):
    pass  # Aqui você pode adicionar funcionalidades específicas no futuro


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def exibir(self, saldo):
        print("\n================ EXTRATO ================")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar(f"{self.data.strftime('%d/%m/%Y %H:%M')} - Depósito: R$ {self.valor:.2f}")
            print(f"\n=== Depósito de R$ {self.valor:.2f} realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if self.valor <= 0:
            print("\n@@@ Valor inválido. @@@")
        elif self.valor > conta.saldo:
            print("\n@@@ Saldo insuficiente. @@@")
        elif self.valor > conta.limite:
            print("\n@@@ Valor do saque excede o limite. @@@")
        elif conta.numero_saques >= conta.limite_saques:
            print("\n@@@ Número de saques excedido. @@@")
        else:
            conta.saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar(f"{self.data.strftime('%d/%m/%Y %H:%M')} - Saque: R$ {self.valor:.2f}")
            print("\n=== Saque realizado com sucesso! ===")


def menu():
    menu = """\n
    =============== MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair
    => """
    return input(textwrap.dedent(menu))

def encontrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario.cpf == cpf), None)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if encontrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
    usuarios.append(usuario)
    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)
    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return None
    conta = ContaCorrente(agencia, numero_conta, usuario)
    print("=== Conta criada com sucesso! ===")
    return conta

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero}")
        print(f"Titular:\t{conta.cliente.nome}")

def selecionar_conta(contas):
    if not contas:
        print("\n@@@ Nenhuma conta encontrada. @@@")
        return None
    for i, conta in enumerate(contas, 1):
        print(f"[{i}] {conta.cliente.nome} - Conta: {conta.numero}")
    indice = int(input("Selecione o número da conta: ")) - 1
    if 0 <= indice < len(contas):
        return contas[indice]
    print("\n@@@ Conta inválida. @@@")
    return None


def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Valor do depósito: "))
                conta.depositar(Deposito(valor))

        elif opcao == "2":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Valor do saque: "))
                conta.sacar(Saque(valor))

        elif opcao == "3":
            conta = selecionar_conta(contas)
            if conta:
                conta.exibir_extrato()

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("\n@@@ Opção inválida! @@@")

main()
