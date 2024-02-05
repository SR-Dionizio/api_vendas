import hook_vendas

def vendas(event, context):
    body = hook_vendas.criar_dados_vendas()
    
    return body

def clientes(event, context):
    body = hook_vendas.criar_dados_clientes()
    
    return body

def produtos(event, context):
    body = hook_vendas.criar_dados_produtos()
    
    return body

def metodos_pagamentos(event, context):
    body = hook_vendas.criar_dados_metodos_pagamento()
    
    return body

def locais(event, context):
    body = hook_vendas.criar_dados_locais()
    
    return body

