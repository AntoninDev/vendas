from os import path, makedirs, system
from datetime import datetime

data_atual = datetime.now().strftime(r"%d/%m/%y")
caminho_da_pasta = 'C:/Users/Admin/Documents/controle_de_estoque'
estoque = []
produtos_estoque = 0
valor_total = 0
def atualizar_estoque():
    global estoque, produtos_estoque, valor_total
    estoque = []
    produtos_estoque = 0
    valor_total = 0
    with open(f'{caminho_da_pasta}/estoque.txt', 'r', encoding='utf-8') as src:
        for item in src:
           item = item.split()
           estoque += [{'nome': item[0], 'valor': float(item[1]), 'data': item[2]}]
           produtos_estoque += 1
           valor_total += float(item[1])
if not path.exists(caminho_da_pasta):
    makedirs(caminho_da_pasta)
    open(f'{caminho_da_pasta}/estoque.txt', 'w', encoding='utf-8')    
else:
    atualizar_estoque()


def limpar_tela():
    system('cls')

def menu():
    print('''===== MENU =====
[1] Consultar estoque
[2] Consultar vendas
[3] Dar baixa em produto
[4] Adicionar produto
[5] Fechar progama\n''') 

def voltar():
    input('Clique ENTER para voltar ao menu principal ')

def linha(n=15):
    print('-'*n)
    
print('CARREGANDO...')
limpar_tela()
while True:
    print('CARREGANDO...')
    limpar_tela()
    menu()
    atualizar_estoque()
    escolha_principal = str(input('Digite sua escolha: '))
    while escolha_principal == '' or escolha_principal.isdigit() == False or int(escolha_principal) > 5 or int(escolha_principal) < 1:
        limpar_tela()
        menu()
        print('Escolha inválida. Escolha um dos números do menu!')
        escolha_principal = str(input('Digite sua escolha: '))
    escolha_principal = int(escolha_principal)
    
    if escolha_principal == 1:
        limpar_tela()
        escolha_estoque = str(input(f'Temos {produtos_estoque} produtos no estoque deseja ver os detalhes? S/N '))
        
        while escolha_estoque == '' or escolha_estoque.strip().upper()[0] != 'S' and escolha_estoque.strip().upper()[0] != 'N':
            limpar_tela()
            print('Escolha inválida. Escolha S ou N') 
            escolha_estoque = str(input(f'Temos {produtos_estoque} produtos no estoque deseja ver os detalhes? S/N '))
            
        if escolha_estoque.strip().upper()[0] == 'S':
            c = 1
            limpar_tela()
            for produto in estoque:
                print(f'{c:-^15}')
                print(f'Nome do produto: {produto['nome']}')
                print(f'Valor: R${produto['valor']:.2f}')
                print(f'Data em que foi adicionado: {produto['data']}')
                c += 1
            linha(14)
            print(f'\nO valor total dos {produtos_estoque} produtos no estoque é de: R$ {valor_total:.2f}\n')    
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
            linha(14)
        voltar()
        limpar_tela()    
    elif escolha_principal == 3:    
        print(3)  
    elif escolha_principal == 4:
            
            while True:
                limpar_tela()
                linha()
                print(f'Adicionar {produtos_estoque+1}º produto ao estoque.')
                print('Para cancelar pressione ENTER.')
                linha()
                nome_produto = str(input('Digite o nome do produto: '))
                if nome_produto == '':
                   limpar_tela()   
                   break
                valor_produto = str(input('Digite o valor do produto: R$ '))
                if valor_produto == '':
                   limpar_tela()   
                   break
                with open(f'{caminho_da_pasta}/estoque.txt', 'a', encoding='utf-8') as src:
                        src.write(f'{nome_produto} {valor_produto} {data_atual}\n')       
                atualizar_estoque()
                limpar_tela()       
                escolha_adicionar = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N ')  
                while escolha_adicionar == "" or escolha_adicionar.strip().upper()[0] != 'S' and escolha_adicionar.strip().upper()[0] != 'N':
                    limpar_tela()
                    print('Escolha inválida. Escolha S ou N')
                    escolha_adicionar = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N ')
                if escolha_adicionar.strip().upper()[0] == 'N':
                 limpar_tela()   
                 break                
    else:
        print('Saindo...')
        break    
    