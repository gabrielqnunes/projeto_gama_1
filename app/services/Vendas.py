import json


def get_vendas(path):
    path = path + '/static/data/Vendas.json'
    vendas = None
    with open(path, 'r') as file:
        vendas = json.load(file)

    print(vendas)

    for venda in vendas:
        total = 0
        for item in venda:
            print(item)
            total += item['preco'] * item['quantidade']
        venda.append(total)
    print(vendas)

    return vendas
