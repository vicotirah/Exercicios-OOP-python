
import os

#Arrays e Dict
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

#Funções
def exibir_nome_do_programa():

    '''Exibe título do programa'''

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_menu():

    '''Exibe menu de opções'''

    print('Opções: \n1. Cadastrar restaurante\n2. Listar restaurante\n3. Alterar status do restaurante\n4. Sair')

def finalizar_app():

    ''' Finaliza o app'''

    exibir_subtitulo('Finalizando o app\n')
    exit()

def voltar_menu():
    '''
    Solicita uma tecla para voltar ao menu principal

    Output:
    - Retorna ao menu principal
    '''

    input('\nDigite uma tecla para voltar ao menu principal ')
    exibir_nome_do_programa()
    exibir_menu()

def exibir_subtitulo (texto):
    '''Exibe subtitulo das opções'''
    os.system('cls')
    print(texto)
    
def opcao_invalida():
    '''
    Informa que a opção escolhida não é válida

    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_menu()

def cadastrar_novo_restaurante():

    '''
    Função responsável por cadastrar novo restaurante
    
    Inputs:
    - Nome do Restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes 
    '''

    exibir_subtitulo("""
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▄░█ █▀█ █░█ █▀█ █▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █░▀█ █▄█ ▀▄▀ █▄█ ▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█\n""")

    nome_restaurante = input('Insira o nome do restaurante: ')
    categoria = input(f'Insira a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado')

    voltar_menu()

def listar_restaurantes():  

    '''
    Função responsável por listar restaurantes cadastrados
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''

    exibir_subtitulo("""
    █░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
    █▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█""")

    print('\nLista de restaurante:\n')
    print(f"{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu()

def alterar_status():

    '''
    Função responsável por ativar ou desativar o status dos restaurantes

    Input:
    - Nome dos restaurante que deseja alterar o status (considera maiúsculas e minúsculas)

    Output:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo("""
    ▄▀█ ▀█▀ █ █░█ ▄▀█ █▀█ ░░▄▀ █▀▄ █▀▀ █▀ ▄▀█ ▀█▀ █ █░█ ▄▀█ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █▀█ ░█░ █ ▀▄▀ █▀█ █▀▄ ▄▀░░ █▄▀ ██▄ ▄█ █▀█ ░█░ █ ▀▄▀ █▀█ █▀▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
    \n""")

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    while True:
        try:
            opcao_escolhida = int(input('\nEscolha a opção desejada: '))
            match opcao_escolhida:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    alterar_status()
                case 4:
                    finalizar_app()
                case _:
                    opcao_invalida()
        except ValueError:
            opcao_invalida() 
        except Exception as e:
            opcao_invalida() 

def main():
    ''' Função principal que inicia o programa '''
    while True:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_menu()
        escolher_opcao()

if __name__ == '__main__':
    main()