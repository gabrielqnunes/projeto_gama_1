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

            produtos = {
                "legumes_e_vegetais": [
                    {"id": 0, "nome": "Cenoura", "preco": 2.12},
                    {"id": 1, "nome": "Cebola", "preco": 2.34},
                    {"id": 2, "nome": "Alface", "preco": 1.89} ,
                    {"id": 3, "nome": "Tomate", "preco": 2.25},
                    {"id": 4, "nome": "Picles", "preco": 5.79},
                    {"id": 5, "nome": "Pepino", "preco": 4.19},
                     {"id": 6, "nome": "Batata", "preco": 3.29},
                ],
                "bebidas": [
                    {"id": 0, "nome": "Cerveja", "preco": 2.23},
                    {"id": 1, "nome": "Kombucha", "preco": 4.13},
                    {"id": 2, "nome": "Chá", "preco": 3.23},
                    {"id": 3, "nome": "Bebidas", "preco": 3.23},
                ],
                "Grãos": [
                    {"id": 0, "nome": "Trigo", "preco": 0.89},
                    {"id": 1, "nome": "Soja em Grão", "preco": 2.21},
                    {"id": 2, "nome": "Grão de Bico", "preco": 2.19},
                    {"id": 3, "nome": "Aveia", "preco": 3.19},
                    {"id": 4, "nome": "Centeio", "preco": 3.13},
                    {"id": 5, "nome": "Sagu", "preco": 2.87},
                    {"id": 6, "nome": "Lentilha Verde" , "preco": 3.19},
                ],
                "Carnes e Frios": [
                    {"id": 0, "nome": "Costela de Porco", "preco": 8.39},
                    {"id": 1, "nome": "Costela de Boi", "preco": 15.45},
                    {"id": 2, "nome": "Filé Mignon de Boi", "preco": 45.45},
                    {"id": 3, "nome": "Filé Mignon de Porco", "preco": 31.33},
                    {"id": 4, "nome": "Cupim", "preco": 3.13},
                    {"id": 5, "nome": "Maminha de Boi", "preco": 17.33},
                    {"id": 6, "nome": "Lentilha Verde" , "preco": 3.19},
                    {"id": 7, "nome": "Queijo" , "preco": 19,21},
                    {"id": 8, "nome": "Presunto" , "preco": 21,19},
                ],
                
                

                
            }

# 4 - Carnes e Frios


# 4.6 Maminha de boi
