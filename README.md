# Sistema Bancário

Este é um sistema bancário simples, desenvolvido em Python, utilizando orientação a objetos para gerenciar clientes e contas bancárias. Os dados são persistidos em um arquivo JSON.

## Estrutura do Projeto

```text
Sistema-Bancario/
│
├── modelos.py         # Classes Cliente e Conta, decoradores, geradores e iteradores personalizados, persistência dos dados
├── sistema.py         # Fluxo principal do sistema (interface de texto)
├── clientes.json      # Arquivo de dados dos clientes e contas
├── testes.py          # Testes automatizados (opcional)
```

## Funcionalidades

- Cadastro de clientes (nome, CPF, endereço)
- Criação de múltiplas contas por cliente
- Depósito, saque e extrato por conta
- Listagem de contas de todos os clientes
- Persistência dos dados em `clientes.json`
- **Registro automático de data, hora e tipo de cada transação** (via decorador)
- **Gerador para iteração e filtragem das transações de uma conta**
- **Iterador personalizado para percorrer todas as contas do banco**

## Novas funcionalidades

- Validação de CPF no cadastro de clientes
- Histórico geral por cliente
- Novo tipo de conta: ContaPoupanca
- Padronização de mensagens de erro e sucesso
- Testes automatizados em `testes.py`

## Como usar

1. **Clone o repositório e acesse a pasta:**

   ```sh
   git clone https://github.com/seu-usuario/Sistema-Bancario.git
   cd Sistema-Bancario
   ```

2. **Execute o sistema:**

   ```sh
   python sistema.py
   ```

3. **Siga o menu interativo para utilizar as funcionalidades.**

## Exemplos de uso avançado

### Iterando sobre todas as contas do banco

```python
from modelos import carregar_clientes, ContaIterador

clientes = carregar_clientes()
for info in ContaIterador(clientes):
    print(info)  # {'titular': ..., 'cpf': ..., 'agencia': ..., 'numero': ..., 'saldo': ...}
```

### Iterando e filtrando transações de uma conta

```python
conta = clientes[0].contas[0]
# Todas as transações
for transacao in conta.transacoes():
    print(transacao)
# Apenas saques
for transacao in conta.transacoes(tipo="Saque"):
    print(transacao)
```

## Requisitos

- Python 3.8 ou superior

---

Desenvolvido por David Barcellos Cardoso para fins didáticos.
