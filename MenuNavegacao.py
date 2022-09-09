from MenuCadastro import MenuCadastro
from MenuRelatorios import MenuRelatorios
from MenuVendas import MenuVendas
from Tela import Tela


class MenuNavegacao:
    def Run(self):
        primeiraExecucao = True
        menuCadastro = MenuCadastro()
        menuRelatorios = MenuRelatorios()
        menuVendas = MenuVendas()
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            if (not primeiraExecucao):
                Tela.LimpaTela()
            print('======================================')
            print('||          MENU NAVEGAÇÃO          ||')
            print('======================================')
            print('|| (1) CADASTRO                     ||')
            print('|| (2) VENDAS                       ||')
            print('|| (3) RELATORIO                    ||')
            print('|| (4) SAIR                         ||')
            print('======================================\n')
            entrada = input('Escolha uma opção: ')

            if (entrada == '1'):
                menuCadastro.Run()

            if (entrada == '2'):
                menuVendas.Run()

            if (entrada == '3'):
                menuRelatorios.Run()

            if (entrada == '4'):
                Tela.LimpaTela()
                continuarExecutando = False

            primeiraExecucao = False
