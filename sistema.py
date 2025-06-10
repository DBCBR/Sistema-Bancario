import clientes as c
import operacoes as o
import locale

# Configurar o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("\nBem-vindo ao Banco do Devs!\n")
print("Por favor, digite seu nome: ")
nome = input()
if nome in c.clientes:
    print("\nOlá, " + nome + "!\n")
    # Reiniciar o contador de saques a cada acesso
    c.clientes[nome]['saques'] = 0
else:
    print("\nCliente não encontrado. Deseja se cadastrar? (s/n)")
    resposta = input()
    if resposta == "s":
        print("\nDigite o seu nome: ")
        nome = input()
        print("Digite o seu saldo: ")
        saldo = float(input())
        c.clientes[nome] = {'saldo': saldo, 'saques': 0, 'historico': []}
        c.salvar_clientes(c.clientes)  # Salvar dados dos clientes
        print("\nCadastro realizado com sucesso!\n")
    else:
        print("\nObrigado e até logo!\n")
        exit()

while True:
    print("\nEscolha a operação: 1-Saque, 2-Depósito, 3-Extrato, 4-Sair")
    try:
        operacao = int(input())
        if operacao == 1:
            print("\nDigite o valor do saque:")
            saque = float(input())
            mensagem = o.saque(c.clientes, nome, saque)
            print("\n" + mensagem + "\n")
        elif operacao == 2:
            print("\nDigite o valor do depósito:")
            deposito = float(input())
            mensagem = o.deposito(c.clientes, nome, deposito)
            print("\n" + mensagem + "\n")
        elif operacao == 3:
            mensagem = o.extrato(c.clientes, nome)
            print("\n" + mensagem + "\n")
        elif operacao == 4:
            print("\nObrigado e até logo!\n")
            break
        else:
            print("\nOperação inválida.\n")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.\n")
