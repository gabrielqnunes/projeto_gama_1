import time
import json
from Tela import Tela
from CarregaProduto import CarregaProduto


class MenuVendas:

    carrinho = []

    def Run(self):
        continuarExecutando = True
        entrada = '-1'

        produtos = CarregaProduto.LoadProduto()

        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||       CARRINHO DE COMPRAS        ||')
            print('======================================')
            for item in self.carrinho:
                print(
                    f'({item["id"]}) - {item["nome"]}: {item["preco"]} x {item["quantidade"]}  = R$ {(item["preco"]*item["quantidade"]):.2f}')
            print('======================================')
            print('|| (1) Adicionar produto no carrinho||')
            print('|| (2) Remover produto do carrinho  ||')
            print('|| (3) Finalizar compra             ||')
            print('|| (4) Sair                         ||')
            print('======================================\n')

            entrada = '-1'

            while int(entrada) not in range(1, 5):
                entrada = input('Escolha uma opção:')
                if int(entrada) not in range(1, 5):
                    print('Opção inválida.\n')

            if (entrada == '1'):
                produtoSelecionado = '-1'
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

                    while produtoSelecionado not in idsDeProdutos:
                        produtoSelecionado = input(
                            'Digite o id do produto que você deseja adicionar no carrinho: ')
                        if produtoSelecionado not in idsDeProdutos:
                            print('Opção inválida.\n')

                    quantidadeDesejada = '-1'

                    while int(quantidadeDesejada) <= 0:
                        quantidadeDesejada = input(
                            'Digite a quantidade do produto que você deseja: ')
                        if int(quantidadeDesejada) <= 0:
                            print('Opção inválida.\n')

                    existe_carrinho = False

                    for item in self.carrinho:
                        if str(item["id"]) == produtoSelecionado:
                            item["quantidade"] = item["quantidade"] + \
                                int(quantidadeDesejada)
                            existe_carrinho = True

                    if not existe_carrinho:
                        for item in produtos:
                            if str(item["id"]) == produtoSelecionado:
                                quantidade = {
                                    "quantidade": int(quantidadeDesejada)}
                                item.update(quantidade)
                                self.carrinho.append(item)

            if (entrada == '2'):
                idsDeProdutos = []
                for item in self.carrinho:
                    idsDeProdutos.append(str(item["id"]))

                idRemovido = '-1'

                while idRemovido not in idsDeProdutos:
                    idRemovido = input(
                        'Digite o id do produto que você deseja remover no carrinho:')
                    if idRemovido not in idsDeProdutos:
                        print('Opção inválida.\n')

                for item in self.carrinho:
                    if str(item['id']) == idRemovido:
                        self.carrinho.remove(item)

            if (entrada == '3'):
                somatorioTotal = 0
                Tela.LimpaTela()
                print('======================================')
                print('||             PAGAMENTO            ||')
                print('======================================')
                for item in self.carrinho:
                    print(
                        f'({item["id"]}) - {item["nome"]}: {item["preco"]} x {item["quantidade"]}  = R$ {item["preco"]*item["quantidade"]}')
                print('======================================')
                for item in self.carrinho:
                    somatorioTotal = item["preco"] * \
                        item["quantidade"] + somatorioTotal
                print(f'TOTAL: R$ {somatorioTotal:.2f}')
                print('======================================')
                print('||   ESCOLHA A FORMA DE PAGAMENTO   ||')
                print('======================================')
                print('|| (1) Dinheiro                     ||')
                print('|| (2) Cartão de débito             ||')
                print('|| (3) Cartão de crédito            ||')
                print('|| (4) Pix                          ||')
                print('|| (5) Voltar ao carrinho de compras||')
                print('======================================\n')

                escolha = '-1'

                while int(escolha) not in range(1, 6):
                    escolha = input('Escolha uma opção:')
                    if int(escolha) not in range(1, 6):
                        print('Opção inválida.\n')

                if int(escolha) in range(1, 5):
                    with open("Vendas.json", "r") as file:
                        vendas = json.load(file)

                    vendas["vendas"].append(self.carrinho)

                    vendas_to_string = json.dumps(
                        vendas, indent=4, ensure_ascii=False)

                    with open("Vendas.json", "w") as file:
                        file.write(vendas_to_string)

                    self.carrinho.clear()
                    Tela.LimpaTela()
                    print('======================================')
                    print('||   OBRIGADA POR COMPRAR CONOSCO!  ||')
                    print('||           VOLTE SEMPRE!          ||')
                    print('======================================')
                    time.sleep(3)
                    return

            if (entrada == '4'):
                continuarExecutando = False
