import json


def get_vendas(path: str) -> list:
    path = path + '/static/data/Vendas.json'
    vendas = None
    with open(path, 'r') as file:
        vendas = json.load(file)

    for venda in vendas:
        total = 0
        for item in venda:
            total += item['preco'] * item['quantity']
        venda.append(total)

    return vendas


def set_vendas(path: str, cart: list) -> None:
    path = path + '/static/data/Vendas.json'
    vendas = None
    with open(path, 'r') as file:
        vendas = json.load(file)
    vendas.append(cart)
    print(cart)
    vendas_json = json.dumps(vendas, indent=4)
    with open(path, 'w') as file:
        file.write(vendas_json)
    return None
