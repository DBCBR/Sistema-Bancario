import json
import datetime
from abc import ABC, abstractmethod


def registrar_transacao(tipo):
    def decorador(func):
        def wrapper(*args, **kwargs):
            agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"[{agora}] Transação: {tipo}")
            return func(*args, **kwargs)
        return wrapper
    return decorador


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @registrar_transacao("Saque")
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.append({
                "tipo": "Saque",
                "valor": self.valor,
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @registrar_transacao("Depósito")
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.append({
                "tipo": "Depósito",
                "valor": self.valor,
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })


class Conta(ABC):
    def __init__(self, agencia, numero, cliente, saldo=0.0, historico=None):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.historico = historico if historico is not None else []

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        print("Valor inválido para depósito.")
        return False

    def to_dict(self):
        return {
            "agencia": self.agencia,
            "numero": self.numero,
            "saldo": self.saldo,
            "historico": self.historico,
            "cliente": self.cliente.cpf
        }

    @staticmethod
    def from_dict(data, clientes):
        cliente = next((c for c in clientes if c.cpf == data["cliente"]), None)
        return ContaCorrente(
            agencia=data["agencia"],
            numero=data["numero"],
            cliente=cliente,
            saldo=data.get("saldo", 0.0),
            historico=data.get("historico", [])
        )


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, saldo=0.0, historico=None, limite=500, limite_saques=3):
        super().__init__(agencia, numero, cliente, saldo, historico)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques = len([t for t in self.historico if t["tipo"] == "Saque"])
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite:
            print("Valor excede o limite por saque.")
        elif saques >= self.limite_saques:
            print("Limite de saques diários atingido.")
        elif valor > 0:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido para saque.")
        return False


class ContaPoupanca(Conta):
    def sacar(self, valor):
        # Sem limite de saques, mas saldo não pode ficar negativo
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido para saque.")
        return False


class Cliente:
    def __init__(self, nome, cpf, endereco, contas=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = contas if contas is not None else []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "contas": [conta.numero for conta in self.contas]
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            nome=data["nome"],
            cpf=data["cpf"],
            endereco=data["endereco"]
        )

    def historico_geral(self):
        for conta in self.contas:
            print(f"\nConta {conta.numero} - Agência {conta.agencia}:")
            for transacao in conta.historico:
                print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f} em {transacao['data']}")


def salvar_dados(clientes, contas, arquivo="clientes.json"):
    data = {
        "clientes": [c.to_dict() for c in clientes],
        "contas": [conta.to_dict() for conta in contas]
    }
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def carregar_dados(arquivo="clientes.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            clientes = [Cliente.from_dict(c) for c in data["clientes"]]
            contas = [ContaCorrente.from_dict(conta, clientes) for conta in data["contas"]]
            # Vincula contas aos clientes
            for cliente in clientes:
                cliente.contas = [c for c in contas if c.cliente and c.cliente.cpf == cliente.cpf]
            return clientes, contas
    except FileNotFoundError:
        return [], []


def validar_cpf(cpf):
    """
    Valida se o CPF possui 11 dígitos numéricos.
    """
    return cpf.isdigit() and len(cpf) == 11
