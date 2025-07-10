from modelos import Cliente, ContaCorrente, ContaPoupanca, Saque, Deposito


def test_deposito():
    cliente = Cliente("Teste", "12345678901", "Rua X")
    conta = ContaCorrente("0001", 1, cliente)
    cliente.adicionar_conta(conta)
    assert conta.depositar(100)
    assert conta.saldo == 100


def test_saque_corrente():
    cliente = Cliente("Teste", "12345678901", "Rua X")
    conta = ContaCorrente("0001", 1, cliente)
    cliente.adicionar_conta(conta)
    conta.depositar(500)
    assert conta.sacar(200)
    assert conta.saldo == 300


def test_saque_poupanca():
    cliente = Cliente("Teste", "12345678901", "Rua X")
    conta = ContaPoupanca("0001", 1, cliente)
    cliente.adicionar_conta(conta)
    conta.depositar(300)
    assert conta.sacar(100)
    assert conta.saldo == 200


def test_limite_transacoes_diarias():
    """Testa o limite de 10 transações diárias"""
    cliente = Cliente("Teste", "12345678901", "Rua X")
    conta = ContaCorrente("0001", 1, cliente)
    cliente.adicionar_conta(conta)

    # Fazer 10 depósitos (limite máximo)
    for i in range(10):
        assert conta.depositar(10), f"Falha no depósito {i+1}"

    # O 11º depósito deve falhar
    assert not conta.depositar(10), "Deveria falhar no 11º depósito"

    # Verificar que foram registradas 10 transações
    assert len(conta.historico) == 10


def test_transacao_com_decorator():
    """Testa se o decorator registra corretamente as transações"""
    cliente = Cliente("Teste Decorator", "98765432109", "Rua Y")
    conta = ContaCorrente("0001", 99, cliente)
    cliente.adicionar_conta(conta)

    # Verificar que a conta está limpa
    assert len(conta.historico) == 0

    # Fazer depósito usando a classe Deposito
    Deposito(100).registrar(conta)
    assert conta.saldo == 100
    assert len(conta.historico) == 1
    assert conta.historico[0]["tipo"] == "Depósito"

    # Fazer saque usando a classe Saque
    Saque(50).registrar(conta)
    assert conta.saldo == 50
    assert len(conta.historico) == 2
    assert conta.historico[1]["tipo"] == "Saque"


if __name__ == "__main__":
    test_deposito()
    test_saque_corrente()
    test_saque_poupanca()
    test_limite_transacoes_diarias()
    test_transacao_com_decorator()
    print("✓ Todos os testes passaram!")
