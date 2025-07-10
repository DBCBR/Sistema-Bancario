# Sistema Bancário

Este é um sistema bancário completo, desenvolvido em Python, utilizando orientação a objetos para gerenciar clientes e contas bancárias. Os dados são persistidos em um arquivo JSON.

## Estrutura do Projeto

```text
Sistema-Bancario/
│
├── modelos.py         # Classes do sistema bancário e persistência de dados
├── sistema.py         # Interface principal do sistema
├── clientes.json      # Arquivo de dados dos clientes e contas
├── testes.py          # Testes unitários
├── README.md          # Documentação do projeto
└── LICENSE            # Licença do projeto
```

## Funcionalidades Principais

### 🏦 Gestão de Clientes e Contas

- Cadastro de clientes (nome, CPF, endereço)
- Validação robusta de CPF
- Criação de contas correntes e poupança
- Múltiplas contas por cliente

### 💰 Operações Bancárias

- **Depósitos** com registro automático
- **Saques** com validações específicas por tipo de conta
- **Extrato detalhado** com data e hora
- **Histórico geral** por cliente

### 🛡️ Controles e Limites

- **Limite de 10 transações diárias** por conta
- **Limite de 3 saques diários** para conta corrente
- **Limite de R$ 500 por saque** para conta corrente
- **Saldo não pode ficar negativo**

### 📊 Recursos Avançados

- **Decorator para logging** de transações
- **Persistência automática** em JSON
- **Tratamento robusto de erros**
- **Compatibilidade com formatos antigos** de dados

## Como usar

1. **Execute o sistema:**

   ```bash
   python sistema.py
   ```

2. **Siga o menu interativo:**

   ```text
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [h] Histórico geral do cliente
   [nc] Nova conta
   [lc] Listar contas
   [nu] Novo usuário
   [q] Sair
   ```

## Testes

Execute os testes unitários para validar o sistema:

```bash
python testes.py
```

Os testes cobrem:

- Operações básicas (depósito, saque)
- Limites de transações diárias
- Funcionalidade do decorator
- Diferentes tipos de conta

## Tipos de Conta

### Conta Corrente

- Limite de R$ 500 por saque
- Máximo 3 saques por dia
- Limite de 10 transações por dia

### Conta Poupança

- Sem limite específico de saques
- Apenas limitação de saldo (não pode ficar negativo)
- Limite de 10 transações por dia

## Requisitos

- Python 3.8 ou superior
- Nenhuma dependência externa

---

Desenvolvido por David Barcellos Cardoso para fins didáticos.
