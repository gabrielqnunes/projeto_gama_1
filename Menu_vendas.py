import os


class MenuVendas:
    def Run(self):
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            os.system('clear')
            print('======================================')
            print('||            MENU VENDAS           ||')
            print('======================================')
            print('|| (1) Adicionar produto no carrinho||')
            print('|| (2) Sair                         ||\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                print('======================================')
                print('||        LISTA DE PRODUTOS         ||')
                print('======================================')

            if (entrada == '2'):
                continuarExecutando = False

            # DESENVOLVER SOLUÇÃO AQUI
