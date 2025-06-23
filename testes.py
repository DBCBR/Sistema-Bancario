from modelos import Cliente, ContaCorrente, ContaPoupanca


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


if __name__ == "__main__":
    test_deposito()
    test_saque_corrente()
    test_saque_poupanca()
    print("Todos os testes passaram!")
