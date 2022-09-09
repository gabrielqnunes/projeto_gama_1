import os


class Tela:
    @staticmethod
    def LimpaTela():
        if (os.name == 'nt'):
            os.system('cls')
        else:
            os.system('clear')
