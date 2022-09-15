from CarregaProduto import CarregaProduto
from Tela import Tela
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
                nome = input(
                    'Digite o nome do produto, ou digite (SAIR) para cancelar: \n')
                nome = nome.title().strip()
                if (nome != 'Sair'):
                    nProduto = []
                    for i in Produtos:
                        nProduto.append(i.get('nome'))
                    while (nome in nProduto):
                        nome = input(
                            'Produto já está cadastrado! Cadastre outro produto:\n')
                        nome = nome.title().strip()
                    preco = float(
                        input('Digite o preço do produto: \n').replace(',', '.'))
                    Produtos.append(
                        dict(id=Produtos[-1]['id']+1, nome=nome, preco=preco))
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
                print('||      ALTERAÇÃO DE PRODUTOS       ||')
                print('======================================')
                print('|| Escolha o filtro de busca        ||')
                print('|| (1) Pesquisa por ID do produto   ||')
                print('|| (2) Pesquisa por NOME do produto ||')
                print('|| (3) Voltar                       ||')
                print('======================================\n')
                ent = input('Escolha uma opção: ')

                if (ent == '1'):
                    listaProd = {}
                    idProduto = int(
                        input('Digite a ID do produto a ser alterado: '))
                    Tela.LimpaTela()
                    contExecutando = True
                    while (contExecutando):
                        for i in range(0, len(Produtos)):
                            if (idProduto == Produtos[i].get('id')):
                                listaProd = dict(id=Produtos[i].get('id'), nome=Produtos[i].get(
                                    'nome'), preco=Produtos[i].get('preco'))
                                indice = i
                                break
                        if (len(listaProd) != 0):
                            Tela.LimpaTela()
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS        ||')
                            print('======================================')
                            print(
                                f'        ID PRODUTO:  {listaProd.get("id")}')
                            print(
                                f' (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                            print(
                                f' (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f' (3) CANCELAR')
                            print('======================================\n')
                            entAlt = input(
                                'Escolha a opção que deseja alterar: ')

                            if (entAlt == '1'):
                                listaProd['nome'] = input(
                                    'Digite o novo nome do produto: \n').title().strip()
                                Produtos[indice] = listaProd
                                Tela.LimpaTela()
                                print('======================================')
                                print('||      ALTERAÇÃO DE PRODUTOS        ||')
                                print('======================================')
                                print(
                                    f'||        ID PRODUTO:  {listaProd.get("id")}')
                                print(
                                    f'|| (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                                print(
                                    f'|| (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                                print(f'|| (3) CANCELAR')
                                print('======================================\n')
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja alterar outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False

                            if (entAlt == '2'):
                                listaProd['preco'] = float(input(
                                    'Digite o novo preço do produto: '))
                                Produtos[indice] = listaProd
                                Tela.LimpaTela()
                                print('======================================')
                                print('||      ALTERAÇÃO DE PRODUTOS        ||')
                                print('======================================')
                                print(
                                    f'||        ID PRODUTO:  {listaProd.get("id")}')
                                print(
                                    f'|| (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                                print(
                                    f'|| (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                                print(f'|| (3) CANCELAR')
                                print('======================================\n')
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja alterar outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False

                            if (entAlt == '3'):
                                return
                        else:
                            novoCadastro = input(
                                'ID não cadastrado. Deseja cadastrar um novo produto? (S/N): ').upper().split()

                            if (novoCadastro == 'S'):
                                CadastroProduto()
                                contExecutando = False
                                continuar = False
                                entrada = '3'

                            elif (novoCadastro == 'N'):
                                contExecutando = False
                                continuar = False
                                entrada = '3'

                if (ent == '2'):
                    listaProd = {}
                    nomeProduto = input(
                        'Digite a NOME do produto a ser alterado: ').strip().title()
                    Tela.LimpaTela()
                    contExecutando = True
                    while (contExecutando):
                        for i in range(0, len(Produtos)):
                            if (nomeProduto == Produtos[i].get('nome')):
                                listaProd = dict(id=Produtos[i].get('id'), nome=Produtos[i].get(
                                    'nome'), preco=Produtos[i].get('preco'))
                                indice = i
                                break
                        if (len(listaProd) != 0):
                            Tela.LimpaTela()
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS       ||')
                            print('======================================')
                            print(
                                f'        ID PRODUTO:  {listaProd.get("id")}')
                            print(
                                f' (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                            print(
                                f' (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f' (3) CANCELAR')
                            print('======================================\n')
                            entAlt = input(
                                'Escolha a opção que deseja alterar: ')

                            if (entAlt == 1):
                                listaProd['nome'] = input(
                                    'Digite o novo nome do produto: \n')
                                atualizaPreco = input(
                                    'Deseja alterar o preço do novo produto? (S/N): \n').strip().upper()
                                if (atualizaPreco == 'S'):
                                    listaProd['preco'] = float(
                                        input('Digite o preço do novo produto: \n').replace(',', '.'))
                                Produtos[indice] = listaProd
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja alterar outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False

                            if (entAlt == '2'):
                                listaProd['preco'] = float(input(
                                    'Digite o novo preço do produto: '))
                                Produtos[indice] = listaProd
                                Tela.LimpaTela()
                                print('======================================')
                                print('||      ALTERAÇÃO DE PRODUTOS        ||')
                                print('======================================')
                                print(
                                    f'        ID PRODUTO:  {listaProd.get("id")}')
                                print(
                                    f' (1)  NOME PRODUTO:  {listaProd.get("nome")}')
                                print(
                                    f' (2) PRECO PRODUTO:  {listaProd.get("preco")}')
                                print(f' (3) CANCELAR')
                                print('======================================\n')
                                print('Produto atualizado com sucesso!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja alterar outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False

                            if (entAlt == '3'):
                                return

                        else:
                            novoCadastroNome = input(
                                'Produto não cadastrado. Deseja cadastrar? (S/N): ').upper().split()
                            novoCadastroNome = novoCadastroNome[0]

                            if (novoCadastroNome == 'S'):
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
                if (ent == '3'):
                    continuar = False

        def RemoverProduto():

            Produtos = CarregaProduto.LoadProduto()
            continuar = True
            while (continuar):
                Tela.LimpaTela()
                print('======================================')
                print('||        LISTA DE PRODUTOS         ||')
                print('======================================')
                for produto in Produtos:
                    print(
                        '  ({}) - {}'.format(produto["id"], produto["nome"]))
                print('======================================')
                print('||      REMOÇÃO DE PRODUTOS         ||')
                print('======================================')
                print('|| Escolha o filtro de busca        ||')
                print('|| (1) Remova por ID do produto     ||')
                print('|| (2) Remova por NOME do produto   ||')
                print('|| (3) Voltar                       ||')
                print('======================================\n')
                ent = input('Escolha uma opção: ')

                if (ent == '1'):
                    listaProd = {}
                    idProduto = int(
                        input('Digite a ID do produto a ser excluido: '))
                    Tela.LimpaTela()
                    contExecutando = True
                    while (contExecutando):
                        for i in range(0, len(Produtos)):
                            if (idProduto == Produtos[i].get('id')):
                                listaProd = dict(id=Produtos[i].get('id'), nome=Produtos[i].get(
                                    'nome'), preco=Produtos[i].get('preco'))
                                indice = i
                                break
                        if (len(listaProd) != 0):
                            Tela.LimpaTela()
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS        ||')
                            print('======================================')
                            print(
                                f'     ID PRODUTO:  {listaProd.get("id")}')
                            print(
                                f'   NOME PRODUTO:  {listaProd.get("nome")}')
                            print(
                                f'  PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f' (1) CANCELAR')
                            print('======================================\n')
                            entAlt = input(
                                'Deseja excluir o produto? (S/N): ').upper().strip()

                            if (entAlt != '1'):

                                Produtos.remove(Produtos[indice])
                                print('Produto Excluído com Sucesso!!!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja excluir outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False
                if (ent == '2'):
                    listaProd = {}
                    nomeProduto = input(
                        'Digite o Nome do produto a ser excluido: ').title().strip()
                    Tela.LimpaTela()
                    contExecutando = True
                    while (contExecutando):
                        for i in range(0, len(Produtos)):
                            if (nomeProduto == Produtos[i].get('nome')):
                                listaProd = dict(id=Produtos[i].get('id'), nome=Produtos[i].get(
                                    'nome'), preco=Produtos[i].get('preco'))
                                indice = i
                                break
                        if (len(listaProd) != 0):
                            Tela.LimpaTela()
                            print('======================================')
                            print('||      ALTERAÇÃO DE PRODUTOS        ||')
                            print('======================================')
                            print(
                                f'     ID PRODUTO:  {listaProd.get("id")}')
                            print(
                                f'   NOME PRODUTO:  {listaProd.get("nome")}')
                            print(
                                f'  PRECO PRODUTO:  {listaProd.get("preco")}')
                            print(f' (1) CANCELAR')
                            print('======================================\n')
                            entAlt = input(
                                'Deseja excluir o produto? (S/N): ').upper().strip()

                            if (entAlt != '1'):

                                Produtos.remove(Produtos[indice])
                                print('Produto Excluído com Sucesso!!!')
                                CarregaProduto.ExportProduto(Produtos)
                                contExecutando = False
                                continuar = input(
                                    'Deseja excluir outro produto? (S/N): ').strip().upper()
                                if (continuar == 'S'):
                                    continuar = True
                                else:
                                    continuar = False
                if (ent == '3'):
                    continuar = False

        while (continuarExecutando):
            Tela.LimpaTela()
            print('======================================')
            print('||           MENU CADASTRO          ||')
            print('======================================')
            print('|| (1) Cadastrar                    ||')
            print('|| (2) Alterar                      ||')
            print('|| (3) Remover                      ||')
            print('|| (4) Voltar                       ||')
            print('======================================\n')
            entrada = input('Escolha uma opção:')

            if (entrada == '1'):
                CadastroProduto()

            if (entrada == '2'):
                AlterarProduto()

            if (entrada == '3'):
                RemoverProduto()

            if (entrada == '4'):
                continuarExecutando = False
