from services.CarregaProduto import CarregaProduto


def cria(path: str, novo_produto: dict) -> None:
    produtos = CarregaProduto.LoadProduto(path)
    novo_produto['id'] = produtos[-1]['id']+1
    produtos.append(novo_produto)
    CarregaProduto.ExportProduto(path, produtos)
    return None


def atualiza():
    return


def deleta():
    return
