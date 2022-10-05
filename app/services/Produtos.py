from services.CarregaProduto import CarregaProduto


def cria(path: str, novo_produto: dict) -> None:
    produtos = CarregaProduto.LoadProduto(path)
    novo_produto['id'] = produtos[-1]['id'] + 1
    produtos.append(novo_produto)
    preco_formatado = round(float(novo_produto['preco'].replace(',', '.')), 2)
    novo_produto["preco"] = float(preco_formatado)
    CarregaProduto.ExportProduto(path, produtos)
    return None


def atualiza(path: str, id: str, nome: str, preco: str) -> None:
    produtos = CarregaProduto.LoadProduto(path)
    for produto in produtos:
        if str(produto['id']) == id:
            produto['nome'] = nome
            preco_formatado = round(float(preco.replace(',', '.')), 2)
            produto['preco'] = preco_formatado

    CarregaProduto.ExportProduto(path, produtos)
    return None


def deleta(path: str, id_produto: str) -> None:
    produtos = CarregaProduto.LoadProduto(path)
    for produto in produtos:
        if str(produto['id']) == id_produto:
            produtos.remove(produto)
    CarregaProduto.ExportProduto(path, produtos)
    return None
