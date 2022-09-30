from MenuCadastro import MenuCadastro
from MenuRelatorios import MenuRelatorios
from Tela import Tela


class MenuNavegacao:
    def Run(self):
        menuCadastro = MenuCadastro()
        menuRelatorios = MenuRelatorios()
        entrada = ''
        while (entrada != '3'):

            Tela.LimpaTela()
            print('======================================')
            print('||          MENU NAVEGAÇÃO          ||')
            print('======================================')
            print('|| (1) Cadastro                     ||')
            print('|| (2) Relatório                    ||')
            print('|| (3) Voltar                       ||')
            print('======================================\n')
            entrada = input('Escolha uma opção: ')

            if (entrada == '1'):
                menuCadastro.Run()

            if (entrada == '2'):
                menuRelatorios.Run()
