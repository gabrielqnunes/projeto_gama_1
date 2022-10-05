import json


class CarregaProduto:
    @staticmethod
    def LoadProduto(path: str) -> list:
        path = path + '/static/data/Produtos.json'
        with open(path, encoding='utf-8') as openfile:
            Produtos = json.load(openfile)
        return Produtos

    def ExportProduto(path: str, produtos: list) -> None:
        path = path + '/static/data/Produtos.json'
        Produtos_txt = json.dumps(produtos, indent=4)
        with open(path, 'w') as df:
            df.write(Produtos_txt)
