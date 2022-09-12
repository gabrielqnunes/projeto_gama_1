from MenuNavegacao import MenuNavegacao
from MenuVendas import MenuVendas

from Tela import Tela


menuNavegacao = MenuNavegacao()
menuVendas = MenuVendas()

Tela.LimpaTela()
print('======================================')
print('||            BEM-VINDO             ||')
print('======================================')
entrada = ''
primeira_iteracao = True
while entrada != '3':
    if not primeira_iteracao:
        Tela.LimpaTela()
    print('======================================')
    print('||          MENU DESEJADO           ||')
    print('======================================')
    print('|| (1) Gerenciamento                ||')
    print('|| (2) Compras                      ||')
    print('|| (3) Sair                         ||')
    print('======================================')
    is_first_iteration = True
    while entrada not in ['1', '2', '3']:
        if not is_first_iteration:
            print('Favor inserir uma opção válida.')
        entrada = input('Escolha um opção: ')
        is_first_iteration = False

    if entrada == '1':
        Tela.LimpaTela()
        menuNavegacao.Run()

    if (entrada == '2'):
        Tela.LimpaTela()
        menuVendas.Run()

    if entrada != '3':
        entrada = ''

    primeira_iteracao = False
