import os


class MenuRelatorios:
    def Run(self):
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            os.system('clear')
            print('======================================')
            print('||          MENU RELATÓRIOS         ||')
            print('======================================')
            print('|| (1) Sair                         ||\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                continuarExecutando = False

            # DESENVOLVER SOLUÇÃO AQUI
