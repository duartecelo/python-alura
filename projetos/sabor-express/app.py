import math
import os

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
    {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
]

def exibir_nome_do_programa():
    '''
    Essa função é responsável por imprimir o título principal do programa (nome do aplicativo)

    Output:
    - Nome do programa
    '''
    print('''
      
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def finalizar_app():
    '''
    Essa função é responsável por encerrar o programa
    '''
    exibir_subtitulo('Encerrando o app\n')

def exibir_opcoes():
    '''
    Essa função é responsável por exibir as opções do menu

    Outputs:
    - Opção 1 do menu
    - Opção 2 do menu
    - Opção 3 do menu
    - Opção 4 do menu

    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    '''
    Essa função é responsável por aguardar a resposta do usuário para o retorno ao menu principal e, consequentemente, voltar a ele

    Input:
    - Confirmação para voltar ao menu principal

    '''
    input('\nClique [ ENTER ] para voltar ao menu principal')
    main()

def opcao_invalida():
    '''
    Essa função é responsável por informar que o usuário digitou uma opção inválida / não existente no menu

    Output:
    - Mensagem de opção inválida
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''
    Essa função é responsável por exibir o subtítulo específico de cada função do menu

    Outputs:
    - Linha de asteriscos
    - Subtítulo específico
    - Linha de asteriscos
    - Linha em branco

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Essa função é responsável por listar todos os restaurantes existentes

    Output:
    - Cabeçalho explicativo de cada coluna da lista/dicionário
    - Dicionário com todos os restaurantes e seus respectivos status e categorias

    '''
    exibir_subtitulo('Listando os restaurantes\n')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativo' if restaurante['ativo'] else 'Desativado'}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''
    Essa função é responsável por alternar o estado de um restaurante, caso existente

    Input:
    - Restaurante que será checado e, consequentemente, ativado ou desativado

    Outputs:
    - Mensagem de confirmação de ativação ou desativação, caso o restaurante exista
    - Mensagem de erro, caso o restaurante não exista
    '''
    exibir_subtitulo('Alternando o estado do restaurante\n')
    restaurante_a_ativar = input('Digite o nome do restaurante que você deseja alternar o estado: ')
    for restaurante in restaurantes:
        if restaurante_a_ativar == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante['nome']} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {restaurante['nome']} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante "{restaurante_a_ativar}" não encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''
    Essa função é responsável por executar as respectivas funções de cada opção do menu
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Função principal que limpa antigos textos do console e, após, inicia o programa
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()