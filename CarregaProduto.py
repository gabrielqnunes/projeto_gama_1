import json


class CarregaProduto:
    @staticmethod
    def LoadProduto():
        with open('Produtos.json', encoding='utf-8') as openfile:
            Produtos = json.load(openfile)
        return Produtos

    def ExportProduto(dict):

        Produtos_txt = json.dumps(dict, indent=4)
        with open('Produtos.json', 'w') as df:
            df.write(Produtos_txt)
