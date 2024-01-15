from os import path, makedirs, system
from datetime import datetime
data_atual = datetime.now().strftime(r"%d/%m/%y")
caminho_da_pasta = 'C:/Users/Admin/Documents/controle_de_estoque'
estoque = []
vendas = []
valor_total_vendas = 0
produtos_vendidos = 0
produtos_estoque = 0
valor_total = 0

if not path.exists(caminho_da_pasta):
    makedirs(caminho_da_pasta)
    open(f'{caminho_da_pasta}/estoque.txt', 'w', encoding='utf-8')
    open(f'{caminho_da_pasta}/vendas.txt', 'w', encoding='utf-8')
    
def atualizar_estoque():
    print('Atualizando estoque...')
    global estoque, produtos_estoque, valor_total
    estoque = []
    produtos_estoque = 0
    valor_total = 0
    try:
        with open(f'{caminho_da_pasta}/estoque.txt', 'r', encoding='utf-8') as src:
            for item in src:
                item = item.split()
                estoque += [{'nome': item[0].replace('-', ' '), 'valor': float(item[1]), 'data': item[2], 'codigo': item[3]}]
                produtos_estoque += 1
                valor_total += float(item[1])
        limpar_tela()        
    except Exception as e:
        print(f'[ERROR] Falha ao ler o arquivo de estoque. COD: {e}')
        print('Caso o poblema continue tire printe dessa tela e envie ao adiministrador.')
        input('Pressione ENTER para reiniciar o progama.')
        
def listar_estoque():
     for produto in estoque:
        linha()
        print(f'Nome do produto: {produto['nome']}')
        print(f'Valor: R${produto['valor']:.2f}')
        print(f'Data em que foi adicionado: {produto['data']}')
        print(f'Código do produto: {produto['codigo']}')
     linha() 
    
def atualizar_vendas():
    print('Atualizando vendas...')
    global vendas, valor_total_vendas, produtos_vendidos
    vendas = []
    valor_total_vendas = 0
    produtos_vendidos = 0
    try:
        with open(f'{caminho_da_pasta}/vendas.txt', 'r', encoding='utf-8') as src:
            for item in src:
                item = item.split()
                vendas += [{'nome': item[0].replace('-', ' '), 'valor': float(item[1]), 'data': item[2], 'codigo': item[3]}]
                produtos_vendidos += 1
                valor_total_vendas += float(item[1])
        limpar_tela()            
    except Exception as e:
        print(f'[ERROR] Falha ao ler o arquivo de estoque. COD: {e}')
        print('Caso o poblema continue tire printe dessa tela e envie ao adiministrador.')
        input('Pressione ENTER para reiniciar o progama.')   
            
def limpar_tela():
    system('cls')

def menu(i=True):
    if i == True:
        limpar_tela()
    print('''===== MENU =====
[1] Consultar estoque
[2] Consultar vendas
[3] Dar baixa em produto
[4] Adicionar produto
[5] Editar listas
[6] Fechar progama\n''') 

def voltar():
    input('Clique ENTER para voltar ao menu principal ')

def linha(n=15):
    print('-'*n)
    
print('CARREGANDO...')
limpar_tela()
try:
    def main():
        while True:
            print('CARREGANDO...')
            menu()
            
            escolha_principal = str(input('Digite sua escolha: '))
            while escolha_principal == '' or escolha_principal.isdigit() == False or int(escolha_principal) > 6 or int(escolha_principal) < 1:
                menu()
                print('Escolha inválida. Escolha um dos números do menu!')
                escolha_principal = str(input('Digite sua escolha: '))
            escolha_principal = int(escolha_principal)
            
            if escolha_principal == 1:
                atualizar_estoque()
                if produtos_estoque == 0:
                    linha()
                    print('Sem produtos no estoque.')
                    linha()
                    voltar()
                    menu()
                else:    
                    escolha_estoque = str(input(f'Temos {produtos_estoque} produtos no estoque deseja ver os detalhes? S/N '))
                    
                    while escolha_estoque == '' or escolha_estoque.strip().upper()[0] != 'S' and escolha_estoque.strip().upper()[0] != 'N':
                        limpar_tela()
                        print('Escolha inválida. Escolha S ou N') 
                        escolha_estoque = str(input(f'Temos {produtos_estoque} produtos no estoque deseja ver os detalhes? S/N '))
                        
                    if escolha_estoque.strip().upper()[0] == 'S':
                        atualizar_estoque()
                        for produto in estoque:
                            linha()
                            print(f'Nome do produto: {produto['nome']}')
                            print(f'Valor: R${produto['valor']:.2f}')
                            print(f'Data em que foi adicionado: {produto['data']}')
                            print(f'Código do produto: {produto['codigo']}')
                        linha()
                        print(f'\nO valor total dos {produtos_estoque} produtos no estoque é de: R$ {valor_total:.2f}\n')    
                        voltar()
                        limpar_tela()
                    else:
                        limpar_tela()   
            elif escolha_principal == 2:
                atualizar_vendas()
                if produtos_vendidos == 0:
                    linha()
                    print('Sem produtos vendidos.')
                    linha()
                    voltar()
                    menu()
                else:
                    escolha_vendas = str(input(f'Temos {produtos_vendidos} produtos vendidos deseja ver os detalhes? S/N '))
                    
                    while escolha_vendas == '' or escolha_vendas.strip().upper()[0] != 'S' and escolha_vendas.strip().upper()[0] != 'N':
                        limpar_tela()
                        print('Escolha inválida. Escolha S ou N') 
                        escolha_vendas = str(input(f'Temos {produtos_vendidos} produtos vendidos deseja ver os detalhes? S/N '))
                        
                    if escolha_vendas.strip().upper()[0] == 'S': 
                        atualizar_vendas()

                        for venda in vendas:
                            linha()
                            print(f'Nome - {venda['nome']}')
                            print(f'Valor - R${venda['valor']:.2f}')
                            print(f'Data da venda - {venda['data']}')
                            print(f'Código do produto: {venda['codigo']}')
                        linha()
                        print(f'\nO valor total dos {produtos_vendidos} produtos vendidos é de: R$ {valor_total_vendas:.2f}\n')
                        voltar()
                        atualizar_vendas()
                    else:
                        limpar_tela()  
            elif escolha_principal == 3:    
                atualizar_estoque()
                if produtos_estoque == 0:
                    linha()
                    print('Sem produtos no estoque para dar baixa.')
                    linha()
                    voltar()
                    menu()
                else:    
                    listar_estoque()
                    produto_baixa = str(input('\nDigite o código do produto para dar baixa (ou pressione ENTER para cancelar): '))
  
                    while produto_baixa.isdigit() == False or int(produto_baixa) < 1 or int(produto_baixa) > produtos_estoque:
                        if produto_baixa == '':
                            break
                        limpar_tela()
                        listar_estoque()
                        print(f'Produto nº {produto_baixa} não existente na lista. Digite um produto válido: ')
                        produto_baixa = str(input('\nDigite o código do produto para dar baixa (ou pressione ENTER para cancelar): '))  
                    if produto_baixa == '':
                        menu()
                    try:
                        produto_baixa = int(produto_baixa)
                        linhas = open(f'{caminho_da_pasta}/estoque.txt', 'r').readlines()
                        linhas_vendas = len(open(f'{caminho_da_pasta}/vendas.txt', 'r').readlines())
                        mudar_codigo = linhas[produto_baixa - 1].split()
                        mudar_codigo[3] = str(f'{linhas_vendas + 1}\n')
                        produto = ' '.join(mudar_codigo)
                        with open(f'{caminho_da_pasta}/vendas.txt', 'a') as src:
                            src.write(produto)
                        linhas_estoque = open(f'{caminho_da_pasta}/estoque.txt', 'r').readlines()
                        linhas_estoque.pop(produto_baixa - 1)
                        c = 0
                        open(f'{caminho_da_pasta}/estoque.txt', 'w')
                        
                        for item in linhas_estoque:
                            mudar_codigo_estoque = item.split()
                            mudar_codigo_estoque[3] = str(f'{c + 1}\n')
                            produto_estoque = ' '.join(mudar_codigo_estoque)
                            c += 1
                            with open(f'{caminho_da_pasta}/estoque.txt', 'a') as src:
                                src.write(produto_estoque)
                        input()
                    except Exception as e:
                        print(e)
                        voltar()
            elif escolha_principal == 4:
                    
                    while True:
                        from re import sub
                        limpar_tela()
                        atualizar_estoque()
                        linha()
                        print(f'Adicionar {produtos_estoque+1}º produto ao estoque.')
                        print('Para cancelar pressione ENTER.')
                        linha()
                        nome_produto = str(input('Digite o nome do produto: '))
                        if nome_produto == '':
                            limpar_tela()   
                            break
                        valor_produto = str(input('Digite o valor do produto: R$ ')).split()[0]
                        print(valor_produto)
                        while valor_produto.isdigit() == False:
                            limpar_tela()
                            linha()
                            print(f'Adicionar {produtos_estoque+1}º produto ao estoque.')
                            print('Para cancelar pressione ENTER.')
                            linha()
                            print(f'Digite o nome do produto: {nome_produto}')
                            print(valor_produto)
                            valor_produto = str(input('Digite o valor do produto: R$ ')).split()[0]
                            
                        if ',' in valor_produto:
                            valor_produto = valor_produto.replace(',', '.')
                        valor_produto = sub(r'\.+', '.', valor_produto)
                        if valor_produto == '':
                            limpar_tela()   
                            break
                        nome_produto = nome_produto.lstrip().rstrip().replace(' ', '-')
                        with open(f'{caminho_da_pasta}/estoque.txt', 'a', encoding='utf-8') as src:
                                src.write(f'{nome_produto} {float(valor_produto):.2f} {data_atual} {produtos_estoque + 1}\n')       
                        atualizar_estoque()
                        limpar_tela()       
                        escolha_adicionar = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N ')  
                        while escolha_adicionar == '' or escolha_adicionar.strip().upper()[0] != 'S' and escolha_adicionar.strip().upper()[0] != 'N':
                            limpar_tela()
                            print('Escolha inválida. Escolha S ou N')
                            escolha_adicionar = input(f'Produto nº{produtos_estoque} adicionado ao estoque. Deseja adicionar mais produtos? S/N ')
                        if escolha_adicionar.strip().upper()[0] == 'N':
                            limpar_tela()   
                            break                
            else:
                print('Saindo...')
                break
    main()             
except Exception as e:
    limpar_tela()
    print(f'[ERROR] Infelizmente ocorreu um erro! COD: {e}')
    print('Caso o poblema continue tire printe dessa tela e envie ao adiministrador.')
    input('Pressione ENTER para reiniciar o progama.')       
    main()
    