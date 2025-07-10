from modelos import (
    Cliente, ContaCorrente, ContaPoupanca, Saque, Deposito,
    salvar_dados, carregar_dados, validar_cpf
)


def menu():
    print("""
[d] Depositar
[s] Sacar
[e] Extrato
[h] Histórico geral do cliente
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
    except (ValueError, IndexError):
        pass
    print("Conta inválida.")
    return None


def main():
    clientes, contas = carregar_dados()
    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            if not validar_cpf(cpf):
                print("CPF inválido! Digite apenas números e 11 dígitos.")
                continue
            endereco = input("Endereço: ")
            if buscar_cliente_por_cpf(clientes, cpf):
                print("CPF já cadastrado.")
            else:
                cliente = Cliente(nome, cpf, endereco)
                clientes.append(cliente)
                print("Cliente cadastrado com sucesso!")
        elif opcao == "nc":
            cpf = input("CPF do titular: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente:
                print("Cliente não encontrado.")
            else:
                numero = len(contas) + 1
                tipo = input("Tipo de conta ([c]orrente/[p]oupança): ").lower()
                if tipo == "p":
                    conta = ContaPoupanca("0001", numero, cliente)
                else:
                    conta = ContaCorrente("0001", numero, cliente)
                contas.append(conta)
                cliente.adicionar_conta(conta)
                print(
                    f"Conta criada: Agência 0001, Número {numero}, Tipo: {'Poupança' if tipo == 'p' else 'Corrente'}")
        elif opcao == "lc":
            for conta in contas:
                print(
                    (
                        f"Titular: {conta.cliente.nome} | Agência: {conta.agencia} | "
                        f"Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}"
                    )
                )
        elif opcao == "d":
            cpf = input("Informe seu CPF: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente or not cliente.contas:
                print("Cliente ou conta não encontrada.")
                continue
            conta = selecionar_conta(cliente)
            if not conta:
                continue
            try:
                valor = float(input("Valor do depósito: "))
            except ValueError:
                print("Valor inválido.")
                continue
            Deposito(valor).registrar(conta)
        elif opcao == "s":
            cpf = input("Informe seu CPF: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente or not cliente.contas:
                print("Cliente ou conta não encontrada.")
                continue
            conta = selecionar_conta(cliente)
            if not conta:
                continue
            try:
                valor = float(input("Valor do saque: "))
            except ValueError:
                print("Valor inválido.")
                continue
            Saque(valor).registrar(conta)
        elif opcao == "e":
            cpf = input("Informe seu CPF: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente or not cliente.contas:
                print("Cliente ou conta não encontrada.")
                continue
            conta = selecionar_conta(cliente)
            if not conta:
                continue
            print("Extrato:")
            if not conta.historico:
                print("Nenhuma transação encontrada.")
            else:
                for transacao in conta.historico:
                    data = transacao.get('data', 'Data não informada')
                    tipo = transacao.get('tipo', 'Tipo não informado')
                    valor = transacao.get('valor', 0.0)
                    print(f"  {tipo}: R$ {valor:.2f} em {data}")
                print(
                    f"Transações realizadas hoje: {conta.contar_transacoes_hoje()}/{conta.limite_transacoes_diarias}")
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        elif opcao == "h":
            cpf = input("Informe seu CPF: ")
            cliente = buscar_cliente_por_cpf(clientes, cpf)
            if not cliente or not cliente.contas:
                print("Cliente ou conta não encontrada.")
                continue
            cliente.historico_geral()
        elif opcao == "q":
            salvar_dados(clientes, contas)
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
