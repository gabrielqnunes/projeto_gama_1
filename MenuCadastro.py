from decimal import InvalidOperation
from pickle import FALSE, TRUE
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
            Produtos = CarregaProduto.LoadProduto()
            continuar = 'S'
            while (continuar != 'N'):
                Tela.LimpaTela()
                print('======================================')
                print('||      CADASTRO DE PRODUTOS        ||')
                print('======================================\n')
                nome = input('Digite o nome do produto, ou digite (SAIR) para cancelar: \n')
                nome = nome.title().strip()
                if(nome != 'Sair'):
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
                    entrada = 3
                    CarregaProduto.ExportProduto(Produtos)
                else:
                    continuar = 'N'
        
        def AlterarProduto():
            Produtos = CarregaProduto.LoadProduto()
            continuar = True
            while (continuar):
                Tela.LimpaTela()
                print('======================================')
                print('||      ALTERAÇÃO DE PRODUTOS        ||')
                print('======================================\n')
                print('|| Escolha o filtro de busca         ||')
                print('|| (1) Pesquisa por ID do produto    ||')
                print('|| (2) Pesquisa por NOME do produto  ||')
                print('|| (3) Sair                          ||')
                ent = input('Escolha uma opção: ')
                
                if(ent == '1'):
                    listaProd = {}
                    idProduto = int(input('Digite a ID do produto a ser alterado: '))
                    Tela.LimpaTela()
                    contExecutando = True
                    while(contExecutando):
                        for i in range(0,len(Produtos)):
                            if(idProduto == Produtos[i].get('id')):
                                listaProd = dict(id = Produtos[i].get('id'),nome = Produtos[i].get('nome'),preco = Produtos[i].get('preco'))
                                indice = i
                                break
                        if(len(listaProd) != 0):
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS        ||')
                            print('======================================')
                            print(f'||        ID PRODUTO:  {listaProd.get("id")}')
                            print(f'|| (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                            print(f'|| (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f'|| (3) CANCELAR')
                            print('======================================\n')
                            entAlt = input('Escolha a opção que deseja alterar: ')

                            if(entAlt == '1'):
                                listaProd['nome'] = input('Digite o novo nome do produto: \n').title().strip()
                                atualizaPreco = input('Deseja alterar o preço do novo produto? (S/N): \n').strip().upper()
                                if(atualizaPreco == 'S'):
                                    listaProd['preco'] = float(input('Digite o preço do novo produto: \n').replace(',','.'))
                                Produtos[indice] = listaProd
                                print('======================================')
                                print('||      ALTERAÇÃO DE PRODUTOS        ||')
                                print('======================================')
                                print(f'||        ID PRODUTO:  {listaProd.get("id")}')
                                print(f'|| (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                                print(f'|| (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                                print(f'|| (3) CANCELAR')
                                print('======================================\n')
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input('Deseja alterar outro produto? (S/N): ').strip().upper()
                                if(continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False
                        else:
                            novoCadastro = input('ID não cadastrado. Deseja cadastrar um novo produto? (S/N): ').upper().split()
                            if(novoCadastro[0] == 'S'):
                                CadastroProduto()
                                contExecutando = False
                                continuar = False
                                entrada = '3'
                                
                            elif(novoCadastro[0] == 'N'):
                                contExecutando = False
                                continuar = False
                                entrada = '3'
                                
                                

                if(ent == '2'):
                    listaProd = {}
                    nomeProduto = input('Digite a NOME do produto a ser alterado: ').strip().title()
                    Tela.LimpaTela()
                    contExecutando = True
                    while(contExecutando):
                        for i in range(0,len(Produtos)):
                            if(nomeProduto == Produtos[i].get('nome')):
                                listaProd = dict(id = Produtos[i].get('id'),nome = Produtos[i].get('nome'),preco = Produtos[i].get('preco'))
                                indice = i
                                break
                        if(len(listaProd) != 0):
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS        ||')
                            print('======================================')
                            print(f'||        ID PRODUTO:  {listaProd.get("id")}')
                            print(f'|| (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                            print(f'|| (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f'|| (3) CANCELAR')
                            print('======================================\n')
                            entAlt = input('Escolha a opção que deseja alterar: ')

                            if(entAlt == 1):
                                listaProd['nome'] = input('Digite o novo nome do produto: \n')
                                atualizaPreco = input('Deseja alterar o preço do novo produto? (S/N): \n').strip().upper()
                                if(atualizaPreco == 'S'):
                                    listaProd['preco'] = float(input('Digite o preço do novo produto: \n').replace(',','.'))
                                Produtos[indice] = listaProd
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input('Deseja alterar outro produto? (S/N): ').strip().upper()
                                if(continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False
                                entrada = 3
                            
                        else:
                            novoCadastro = input('Produto não cadastrado. Deseja cadastrar? (S/N): ').upper().split()
                            if(novoCadastro == 'S'):
                                CadastroProduto()
                                entAlt = '3'
                                contExecutando = False
                                continuarExecutando = False
                                entrada = '3'
                                break
                            else:
                                entAlt = '3'
                                contExecutando = False
                                continuarExecutando = False
                                entrada = '3'
                                break        
                if(ent == '3'):
                    continuar = False

        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||           MENU CADASTRO          ||')
            print('======================================')
            print('|| (1) Cadastrar                    ||')
            print('|| (2) Alterar                      ||')
            print('|| (3) Sair                         ||\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                CadastroProduto()
            
            if(entrada == '2'):
                AlterarProduto()

            if (entrada == '3'):
                continuarExecutando = False
