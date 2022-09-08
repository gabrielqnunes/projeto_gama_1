from Menu_cadastro import MenuCadastro
from Menu_relatorios import MenuRelatorios
from Menu_vendas import MenuVendas


class MenuNavegacao:
    def Run(self):
        menuCadastro = MenuCadastro()
        menuRelatorios = MenuRelatorios()
        menuVendas = MenuVendas()
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            print('======================================')
            print('||          MENU NAVEGAÇÃO          ||')
            print('======================================')
            print('|| (1) CADASTRO                     ||')
            print('|| (2) VENDAS                       ||')
            print('|| (3) RELATORIO                    ||')
            print('|| (4) SAIR                         ||')
            print('======================================')
            entrada = int(input('Escolha uma opção: '))

            if (entrada == 1):
                menuCadastro.Run()

            if (entrada == 2):
                menuVendas.Run()

            if (entrada == 3):
                menuRelatorios.Run()

            if (entrada == 4):
                continuarExecutando = False
