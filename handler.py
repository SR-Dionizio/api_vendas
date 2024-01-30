import hook_vendas
import json

def hello(event, context):
    body = hook_vendas.criar_dados_vendas()
    
    return body
