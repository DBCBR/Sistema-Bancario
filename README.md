# Sistema Bancário

Este é um sistema bancário simples, desenvolvido em Python, utilizando orientação a objetos para gerenciar clientes e contas bancárias. Os dados são persistidos em um arquivo JSON.

## Estrutura do Projeto

```
Sistema-Bancario/
│
├── modelos.py         # Classes Cliente e Conta, persistência dos dados
├── sistema.py         # Fluxo principal do sistema (interface de texto)
├── clientes.json      # Arquivo de dados dos clientes e contas
└── migrar_dados.py    # (Opcional) Script para migrar dados antigos
```

## Funcionalidades

- Cadastro de clientes (nome, CPF, endereço)
- Criação de múltiplas contas por cliente
- Depósito, saque e extrato por conta
- Listagem de contas de todos os clientes
- Persistência dos dados em `clientes.json`

## Como usar

1. **Clone o repositório e acesse a pasta:**
   ```sh
   git clone https://github.com/seu-usuario/Sistema-Bancario.git
   cd Sistema-Bancario
   ```

2. **(Opcional) Migre dados antigos:**
   Se você possui um `clientes.json` antigo, execute:
   ```sh
   python migrar_dados.py
   ```

3. **Execute o sistema:**
   ```sh
   python sistema.py
   ```

4. **Siga o menu interativo para utilizar as funcionalidades.**

## Requisitos

- Python 3.8 ou superior

## Observações

- Os arquivos `clientes.py`, `operacoes.py` e `desafio.py` **não são mais necessários** e podem ser removidos.
- O arquivo `migrar_dados.py` é útil apenas para migração de dados antigos. Após a migração, pode ser excluído.

---

Desenvolvido para fins didáticos.