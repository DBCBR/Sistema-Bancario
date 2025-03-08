import json

# Carregar dados dos clientes de um arquivo JSON
def carregar_clientes():
    try:
        with open('clientes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Salvar dados dos clientes em um arquivo JSON
def salvar_clientes(clientes):
    with open('clientes.json', 'w') as file:
        json.dump(clientes, file, indent=4)

# Inicializar clientes
clientes = carregar_clientes()