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