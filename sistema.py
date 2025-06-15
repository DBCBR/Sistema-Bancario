from modelos import Cliente, Conta, salvar_clientes, carregar_clientes


def menu():
    print("""
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
""")


def buscar_cliente_por_cpf(clientes, cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def selecionar_conta(cliente):
    if not cliente.contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Contas disponíveis:")
    for idx, conta in enumerate(cliente.contas, 1):
        print(
            f"{idx} - Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")
    try:
        escolha = int(input("Escolha o número da conta: "))
        if 1 <= escolha <= len(cliente.contas):
            return cliente.contas[escolha - 1]
    except ValueError:
        pass
    print("Conta inválida.")
    return None


def main():
    clientes = carregar_clientes()
    saques_realizados = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            if buscar_cliente_por_cpf(clientes, cpf):
                print("CPF já cadastrado.")
            else:
                cliente = Cliente(nome, cpf, endereco)
                clientes.append(cliente)
                salvar_clientes(clientes)
                print("Cliente cadastrado com sucesso!")
        elif opcao == "nc":
            cpf = input("CPF do titular: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente:
                print("Cliente não encontrado.")
            else:
                numero = len(cliente.contas) + 1
                conta = Conta("0001", numero)
                cliente.adicionar_conta(conta)
                salvar_clientes(clientes)
                print(f"Conta criada: Agência 0001, Número {numero}")
        elif opcao == "lc":
            for cliente in clientes:
                print(f"Cliente: {cliente.nome} (CPF: {cliente.cpf})")
                cliente.listar_contas()
        elif opcao in ["d", "s", "e"]:
            cpf = input("Informe seu CPF: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            conta = selecionar_conta(cliente)
            if not conta:
                continue
            if opcao == "d":
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            elif opcao == "s":
                valor = float(input("Valor do saque: "))
                chave = f"{cpf}-{conta.numero}"
                saques = saques_realizados.get(chave, 0)
                if conta.sacar(valor, saques_realizados=saques):
                    saques_realizados[chave] = saques + 1
            elif opcao == "e":
                conta.extrato()
            salvar_clientes(clientes)
        elif opcao == "q":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
