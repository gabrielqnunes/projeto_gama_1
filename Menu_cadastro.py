import os


class MenuCadastro:
    def Run(self):
        continuarExecutando = True
        entrada = 0
        while (continuarExecutando):
            os.system('clear')
            print('======================================')
            print('||           MENU CADASTRO          ||')
            print('======================================')
            print('|| (1) Sair                         ||\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                continuarExecutando = False

            # DESENVOLVER SOLUÇÃO AQUI
