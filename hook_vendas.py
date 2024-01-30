from faker import Faker
import random
import json

faker = Faker('pt_BR')

def criar_dados_clientes():
    dados_clientes = []
    for cliente_id in range(1, 100 + 1):
        cliente = {
            'Cliente_ID': cliente_id,
            'Nome': faker.name()
        }
        dados_clientes.append(cliente)
    return dados_clientes

def criar_dados_produtos():
    produtos_saude = ['Seringa', 'Algodão', 'Luvas', 'Microscópio', 'Bisturi', 'Cuba de Vidro', 'Agulha', 'Tubo de Ensaio', 'Pipeta', 'Erlenmeyer']
    dados_produtos = []
    for produto_id in range(1, 11):
        produto = {
            'Produto_ID': produto_id,
            'Nome_Produto': random.choice(produtos_saude)
        }
        dados_produtos.append(produto)
    return dados_produtos

def criar_dados_metodos_pagamento():
    dados_metodos_pagamento = []
    nomes_metodos = ['Cartão de Crédito', 'Boleto', 'Transferência', 'Pix']

    for metodo_id in range(1, 5):
        metodo_pagamento = {
            'Metodo_ID': metodo_id,
            'Nome_Metodo': nomes_metodos[metodo_id - 1]
        }
        dados_metodos_pagamento.append(metodo_pagamento)
    return dados_metodos_pagamento

def criar_dados_locais():
    dados_locais = []
    for local_id in range(1, 50):
        local = {
            'Local_ID': local_id,
            'Nome_Local': faker.city()
        }
        dados_locais.append(local)
    return dados_locais

def criar_dados_vendas():
    dados_vendas = []
    for _ in range(500):
        venda = {
            'Cliente_ID': random.randint(1, 70),
            'Produto_ID': random.randint(1, 10),
            'Quantidade': random.randint(1, 10),
            'Preco_Unitario': random.uniform(10, 100),
            'Data_Compra': faker.date_between(start_date='-1y', end_date='today'),
            'Metodo_Pagamento_ID': random.randint(1, 4),
            'Local_ID': random.randint(1, 5)
        }
        dados_vendas.append(venda)
        dados_vendas_json = json.dumps(dados_vendas, default=str)
        
    return dados_vendas_json


