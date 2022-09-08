class MenuVendas:
    def Run(self):
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            print('\n\n')
            print('======================================')
            print('||            MENU VENDAS           ||')
            print('======================================')
            print('|| (1) Sair                         ||\n')
            entrada = int(input('Escolha uma opção:'))

            if (entrada == 1):
                continuarExecutando = False

            # DESENVOLVER SOLUÇÃO AQUI
