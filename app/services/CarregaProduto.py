import json


class CarregaProduto:
    @staticmethod
    def LoadProduto(path):
        path = path + '/static/data/Produtos.json'
        print(path)
        with open(path, encoding='utf-8') as openfile:
            Produtos = json.load(openfile)
        return Produtos

    def ExportProduto(path, dict):
        path = path + '/static/data/Produtos.json'
        Produtos_txt = json.dumps(dict, indent=4)
        with open(path, 'w') as df:
            df.write(Produtos_txt)
