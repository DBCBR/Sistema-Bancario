# Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python. Ele permite que os usuários realizem operações bancárias básicas, como saques, depósitos e visualização de extratos. Os dados dos clientes são armazenados em um arquivo JSON para persistência.

## Funcionalidades

- Cadastro de novos clientes
- Saque (limite de 3 saques por acesso)
- Depósito
- Visualização de extrato com histórico de transações

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/Sistema-Bancario.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Sistema-Bancario
    ```

## Uso

1. Execute o script `sistema.py`:
    ```bash
    python sistema.py
    ```

2. Siga as instruções no terminal para realizar operações bancárias.

## Estrutura do Projeto

- `sistema.py`: Script principal que gerencia a interação com o usuário.
- `clientes.py`: Módulo que gerencia o carregamento e salvamento dos dados dos clientes.
- `operacoes.py`: Módulo que contém as funções para realizar as operações bancárias.

## Exemplo de Uso

```plaintext
Bem-vindo ao Banco do Devs!

Por favor, digite seu nome:
David

Olá, David!

Escolha a operação: 1-Saque, 2-Depósito, 3-Extrato, 4-Sair
1

Digite o valor do saque:
500

Saque realizado com sucesso. Novo saldo: R$ 1.000,00

Escolha a operação: 1-Saque, 2-Depósito, 3-Extrato, 4-Sair
3

Nome: David
Saldo: R$ 1.000,00
Histórico de transações:
01/01/2025 12:00:00 - Saque: R$ 500,00

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


Este [README.md](http://_vscodecontentref_/1) fornece uma visão geral do projeto, instruções de instalação e uso, e um exemplo de como o sistema funciona. Sinta-se à vontade para ajustar conforme necessário para se adequar ao seu projeto específico.