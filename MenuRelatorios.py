import json
from Tela import Tela


class MenuRelatorios:
    def Run(self):
        Tela.LimpaTela()
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||          MENU RELATÓRIOS         ||')
            print('======================================')
            print('|| (1) Últimas vendas               ||')
            print('|| (2) Voltar                       ||')
            print('======================================\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                with open('Vendas.json', 'r') as file:
                    vendasFile = json.load(file)
                    vendas = vendasFile["vendas"]

                for venda in vendas:
                    Tela.LimpaTela()
                    print('======================================')
                    preco_total = 0
                    for item in venda:
                        print('{} x {} = R$ {:.2f}'.format(
                            item["preco"], item["quantidade"], item["preco"] * item["quantidade"]))
                        preco_total = preco_total + \
                            (item["preco"] * item["quantidade"])
                    print('======================================')
                    print('TOTAL: R$ {:.2f}'.format(preco_total))
                    print('======================================')
                    print('|| (1) Próxima compra                ||')
                    print('|| (2) Voltar                        ||')
                    print('======================================')
                    continua_lista = ''
                    while continua_lista not in ['1', '2']:
                        continua_lista = input('Escolha um opção: ')
                    if continua_lista == '2':
                        break

            if (entrada == '2'):
                continuarExecutando = False
