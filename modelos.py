import json


class Conta:
    def __init__(self, agencia, numero, saldo=0.0, historico=None):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.historico = historico if historico is not None else []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append({"tipo": "Depósito", "valor": valor})
            print("Depósito realizado com sucesso!")
            return True
        print("Valor inválido para depósito.")
        return False

    def sacar(self, valor, limite=500, limite_saques=3, saques_realizados=0):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor excede o limite por saque.")
        elif saques_realizados >= limite_saques:
            print("Limite de saques diários atingido.")
        elif valor > 0:
            self.saldo -= valor
            self.historico.append({"tipo": "Saque", "valor": valor})
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido para saque.")
        return False

    def extrato(self):
        print(f"Extrato da conta {self.numero}:")
        if not self.historico:
            print("Nenhuma movimentação.")
        else:
            for op in self.historico:
                print(f"{op['tipo']}: R$ {op['valor']:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def to_dict(self):
        return {
            "agencia": self.agencia,
            "numero": self.numero,
            "saldo": self.saldo,
            "historico": self.historico
        }

    @staticmethod
    def from_dict(data):
        return Conta(
            agencia=data["agencia"],
            numero=data["numero"],
            saldo=data.get("saldo", 0.0),
            historico=data.get("historico", [])
        )


class Cliente:
    def __init__(self, nome, cpf, endereco, contas=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = contas if contas is not None else []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        for conta in self.contas:
            print(
                f"Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "contas": [conta.to_dict() for conta in self.contas]
        }

    @staticmethod
    def from_dict(data):
        contas = [Conta.from_dict(c) for c in data.get("contas", [])]
        return Cliente(
            nome=data["nome"],
            cpf=data["cpf"],
            endereco=data["endereco"],
            contas=contas
        )


def salvar_clientes(clientes, arquivo="clientes.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in clientes],
                  f, ensure_ascii=False, indent=4)


def carregar_clientes(arquivo="clientes.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [Cliente.from_dict(c) for c in dados]
    except FileNotFoundError:
        return []
