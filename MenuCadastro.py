from CarregaProduto import CarregaProduto
from Tela import Tela
from email import contentmanager
from math import prod
from CarregaProduto import CarregaProduto

class MenuCadastro:
    def Run(self):
        continuarExecutando = True
        entrada = 0

        def CadastroProduto():
            Tela.LimpaTela()

            Produtos = CarregaProduto.LoadProduto()

            contExecutando = True

            Tela.LimpaTela()
            continuar = 'S'
            while (continuar != 'N'):
                Tela.LimpaTela()
                print('======================================')
                print('||      CADASTRO DE PRODUTOS        ||')
                print('======================================\n')
                nome = input('Digite o nome do produto: \n')
                nome = nome.title().strip()
                nProduto = []
                for i in Produtos:
                    nProduto.append(i.get('nome'))
                while (nome in nProduto):
                    nome = input(
                        'Produto já está cadastrado! Cadastre outro produto:\n')
                    nome = nome.title().strip()
                preco = float(
                    input('Digite o preço do produto: \n').replace(',', '.'))
                Produtos.append(dict(id=Produtos[-1]['id']+1,nome=nome,preco=preco))
                continuar = input(
                    'Produto cadastrado com sucesso!\nDeseja cadastrar outro produto?(S/N): ').upper()
                entrada = 2
                CarregaProduto.ExportProduto(Produtos)

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
                entrada = 2

            if (entrada == '2'):
                continuarExecutando = False
