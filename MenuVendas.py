from Tela import Tela


class MenuVendas:

    carrinho = []

    def Run(self):
        continuarExecutando = True
        entrada = 0
        produtos = [

            {"id": 0, "nome": "Cenoura", "preco": 2.12},
            {"id": 1, "nome": "Cebola", "preco": 2.34},
            {"id": 2, "nome": "Alface", "preco": 1.89},
            {"id": 3, "nome": "Tomate", "preco": 2.25},
            {"id": 4, "nome": "Picles", "preco": 5.79},
            {"id": 5, "nome": "Pepino", "preco": 4.19},
            {"id": 6, "nome": "Batata", "preco": 3.29},

        ]

        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||       CARRINHO DE COMPRAS        ||')
            print('======================================')
            for item in self.carrinho:
                print(
                    f'({item["id"]}) - {item["nome"]}: {item["preco"]} x {item["quantidade"]}  = R$ {item["preco"]*item["quantidade"]}')
            print('======================================')
            print('|| (1) Adicionar produto no carrinho||')
            print('|| (2) Remover produto do carrinho  ||')
            print('|| (3) Finalizar compra             ||')
            print('|| (4) Sair                         ||\n')

            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                produtoSelecionado = -1
                idsDeProdutos = []
                for item in produtos:
                    idsDeProdutos.append(str(item["id"]))
                while produtoSelecionado not in idsDeProdutos:
                    Tela.LimpaTela()
                    print('======================================')
                    print('||        LISTA DE PRODUTOS         ||')
                    print('======================================')

                    for item in produtos:
                        print(
                            f'({item["id"]}) - {item["nome"]}: R$ {item["preco"]}')
                    print('======================================')

                    produtoSelecionado = input(
                        'Digite o id do produto que você deseja adicionar no carrinho: ')
                    quantidadeDesejada = input(
                        'Digite a quantidade do produto que você deseja: ')

                    for item in produtos:
                        if str(item["id"]) == produtoSelecionado:
                            quantidade = {
                                "quantidade": int(quantidadeDesejada)}
                            item.update(quantidade)
                            self.carrinho.append(item)

            if (entrada == '2'):
                idRemovido = input(
                    'Digite o id do produto que você deseja remover no carrinho:')
                for item in self.carrinho:
                    if str(item['id']) == idRemovido:
                        self.carrinho.remove(item)

            if (entrada == '4'):
                continuarExecutando = False

            # DESENVOLVER SOLUÇÃO AQUI
