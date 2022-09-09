from Tela import Tela
from email import contentmanager
from math import prod
import json


class MenuCadastro:
    def Run(self):
        continuarExecutando = True
        entrada = 0

        def CadastroProduto():
            Tela.LimpaTela()
            with open('Produtos.json', 'r') as openfile:
                produtos = json.load(openfile)

            contExecutando = True
            ent = 0

            while (contExecutando):
                Tela.LimpaTela()
                print('======================================')
                print('||      CADASTRO DE PRODUTOS        ||')
                print('======================================')
                print('|| (1) Cadastrar                    ||')
                print('|| (2) Alterar                      ||')
                print('|| (3) Excluir                      ||')
                print('|| (4) Sair                         ||\n')
                ent = input('Escolha uma opção: ')

                if (ent == '1'):
                    continuar = 'S'
                    while (continuar != 'N'):
                        Tela.LimpaTela()
                        print('======================================')
                        print('||      CADASTRO DE PRODUTOS        ||')
                        print('======================================\n')
                        nome = input('Digite o nome do produto: \n')
                        nome = nome.title().strip()
                        while (nome in produtos['nome']):
                            nome = input(
                                'Produto já está cadastrado! Cadastre outro produto:\n')
                            nome = nome.title().strip()
                        preco = float(
                            input('Digite o preço do produto: \n').replace(',', '.'))
                        produtos['id'].append(produtos['id'][-1]+1)
                        produtos['nome'].append(nome)
                        produtos['preco'].append(preco)
                        print(produtos)
                        continuar = input(
                            'Produto cadastrado com sucesso!\nDeseja cadastrar outro produto?(S/N): ').upper()
                        ent = 0
                        Produtos = json.dumps(produtos, indent=4)
                        with open('Produtos.json', 'w') as df:
                            df.write(Produtos)

                if (ent == '4'):
                    contExecutando = False

        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||           MENU CADASTRO          ||')
            print('======================================')
            print('|| (1) Cadastrar                    ||')
            print('|| (2) Sair                         ||\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                CadastroProduto()
                entrada = 0

            if (entrada == '2'):
                continuarExecutando = False
