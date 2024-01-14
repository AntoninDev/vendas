from os import path, makedirs, system
from datetime import datetime
data_atual = datetime.now().strftime(r"%d/%m/%y")
caminho_da_pasta = 'C:/Users/Admin/Documents/controle_de_estoque'
estoque = []
def atualizar_estoque():
    global estoque
    with open(f'{caminho_da_pasta}/estoque.txt', 'r', encoding='utf-8') as src:
        for item in src:
           item = item.split()
           estoque += [{'nome': item[0], 'valor': float(item[1]), 'data': item[2]}]
        
if not path.exists(caminho_da_pasta):
    makedirs(caminho_da_pasta)
    open(f'{caminho_da_pasta}/estoque.txt', 'w', encoding='utf-8')    
else:
    atualizar_estoque()

produtos_estoque = len(estoque)
def limpar_tela():
    system('cls')

def menu():
       
    print('''===== MENU =====
[1] Consultar estoque
[2] Consultar vendas
[3] Dar baixa em produto
[4] Adicionar produto
[5] Fechar progama
            ''') 

def voltar():
    input('Clique ENTER para voltar ao menu principal')


vendas = [
    {'produto_vendido': 'short', 'valor': 23, 'data_venda': '12/07/23'},
    {'produto_vendido': 'saia re', 'valor': 55, 'data_venda': '12/07/23'},
    {'produto_vendido': 'touca', 'valor': 100, 'data_venda': '12/07/23'}
]
while True:
    menu()
    escolha_principal = str(input('Digite sua escolha: '))
    while escolha_principal == '' or escolha_principal.isdigit() == False or int(escolha_principal) > 5 or int(escolha_principal) < 1:
        limpar_tela()
        menu()
        print('Escolha inválida. Escolha um dos números do menu!')
        escolha_principal = str(input('Digite sua escolha: '))
    escolha_principal = int(escolha_principal)
    
    if escolha_principal == 1:
        limpar_tela()
        escolha_estoque = str(input(f'Temos {produtos_estoque}  produtos no estoque deseja ver os detalhes? S/N '))
        
        while escolha_estoque == "" or escolha_estoque.strip().upper()[0] != 'S' and escolha_estoque.strip().upper()[0] != 'N':
            limpar_tela()
            print('Escolha inválida. Escolha S ou N') 
            escolha_estoque = str(input(f'Temos {produtos_estoque} produtos no estoque deseja ver os detalhes? S/N '))
            
        if escolha_estoque.strip().upper()[0] == 'S':
            c = 1
            limpar_tela()
            for produto in estoque:
                print(f'{c} - {produto['nome']}')
                print(f'Valor: R${produto['valor']:.2f}')
                print('-'*14)
                c += 1
            voltar()
            limpar_tela()
        else:
           limpar_tela()   
    elif escolha_principal == 2:
        limpar_tela()
        for venda in vendas:
            print(f'Nome - {venda['produto_vendido']}')
            print(f'Valor - R${venda['valor']:.2f}')
            print(f'Data da venda - {venda['data_venda']}')
            print('-'*14)
        voltar()
        limpar_tela()    
    elif escolha_principal == 3:    
        print(3)  
    elif escolha_principal == 4:
            
            while True:
                limpar_tela()
                nome_produto = str(input('Digite o nome do produto: '))
                valor_produto = str(input('Digite o valor do produto: R$ '))
                
                with open(f'{caminho_da_pasta}/estoque.txt', 'a', encoding='utf-8') as src:
                        src.write(f'{nome_produto} {valor_produto} {data_atual}\n')
                atualizar_estoque()        
                e = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N')  
                while e == "" or e.strip().upper()[0] != 'S' and e.strip().upper()[0] != 'N':
                    limpar_tela()
                    print('Escolha inválida. Escolha S ou N')
                    e = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N')            
    else:
        print('Saindo...')
        break    
    