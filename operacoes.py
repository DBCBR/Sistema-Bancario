import clientes as c
import locale
from datetime import datetime

# Configurar o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def saque(clientes, nome, valor):
    if 'saques' not in clientes[nome]:
        clientes[nome]['saques'] = 0

    if clientes[nome]['saques'] >= 3:
        return ("Limite de saques excedido. "
                "Você só pode realizar 3 saques por acesso.")

    if valor > clientes[nome]['saldo']:
        return "Saldo insuficiente."
    else:
        clientes[nome]['saldo'] -= valor
        clientes[nome]['saques'] += 1
        if 'historico' not in clientes[nome]:
            clientes[nome]['historico'] = []
        clientes[nome]['historico'].append({
            'tipo': 'Saque',
            'valor': valor,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
        c.salvar_clientes(clientes)  # Salvar dados dos clientes
        return (
            f"Saque realizado com sucesso. Novo saldo: "
            f"{locale.currency(clientes[nome]['saldo'], grouping=True)}"
        )


def deposito(clientes, nome, valor):
    clientes[nome]['saldo'] += valor
    if 'historico' not in clientes[nome]:
        clientes[nome]['historico'] = []
    clientes[nome]['historico'].append({
        'tipo': 'Depósito',
        'valor': valor,
        'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    })
    c.salvar_clientes(clientes)  # Salvar dados dos clientes
    return (
        f"Depósito realizado com sucesso. Novo saldo: "
        f"{locale.currency(clientes[nome]['saldo'], grouping=True)}"
    )


def extrato(clientes, nome):
    historico = clientes[nome].get('historico', [])
    extrato = (
        f"Nome: {nome}\n"
        f"Saldo: {locale.currency(clientes[nome]['saldo'], grouping=True)}\n"
        "Histórico de transações:\n"
    )
    for transacao in historico:
        extrato += (
            f"{transacao['data']} - {transacao['tipo']}: "
            f"{locale.currency(transacao['valor'], grouping=True)}\n"
        )
    return extrato
