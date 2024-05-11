import jogo as j
import fileHandler as fH

def mostra_menu():
    print('=' * 30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('=' * 30)

arquivo = 'score.txt'
if fH.existe_arquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo não existe.')
    fH.cria_arquivo(arquivo)

while True:
    mostra_menu()
    opcao = (input('Escolha a opção [1/2/3]: '))

    match (opcao):
        case '1':
            print('Iniciar jogo!')
            j.jogar()
        case '2':
            print('SCORE')
            dados = fH.listar_arquivo('score.txt')
            if not dados:
                print('Score vazio.')
            else:
                i = 1
                for jogador in dados:
                    nome, pontuacao = jogador.strip().split(';')  # Divide a linha em nome e pontuação
                    print(f'{i} -> {nome}, pontuação: {pontuacao}.')
                    i += 1
        case '3':
            print('Saindo do jogo. Até mais!')
            break
        case _:
            print('Opção inválida, tente outra.')    