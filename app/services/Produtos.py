from CarregaProduto import CarregaProduto
import os


def cria(path: str, novo_produto: dict) -> None:
    produtos = CarregaProduto.LoadProduto(path)
    novo_produto['id'] = produtos[-1]['id']+1
    produtos.append(novo_produto)
    CarregaProduto.ExportProduto({produtos})
    return None


cria({})


def atualiza():
    return


def deleta():
    return
