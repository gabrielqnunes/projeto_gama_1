import json


def get_vendas(path):
    path = path + '/static/data/Vendas.json'
    vendas = None
    with open(path, 'r') as file:
        vendas = json.load(file)
    return vendas
