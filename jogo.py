import desenhos as d
import fileHandler as fH
from random import choice

# Funções
def jogar():
    lista_palavras = list()
    arquivo = fH.abrir_arquivo('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

palavra_sorteada = choice(lista_palavras)

for x in range(50):
    print()

digitadas = []
acertos = []
erros = 0

nome = input('Quem está jogando? ')

while True:
    adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

    # Condição de vitória
    if adivinha == palavra_sorteada:
        print('Você acertou!')
        break

    # Tentativas
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já usou essa letra!')
        continue
    else:
        digitadas += tentativa # ou append
        if tentativa in palavra_sorteada:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')

    score = d.desenhar_forca(erros)

    # Condição de fim de jogo
    if erros == 6:
        print('      ENFORCADO!            ')
        print()
        print("    _______________         ")
        print("   /               \\       ") 
        print("  /                 \\      ")
        print("//                   \\/\\  ")
        print("\\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \\__      XXX      __/     ")
        print("   |\\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \\_             _/       ")
        print("     \\_         _/         ")
        print("       \\_______/           ")
        print()
        print(f'A palavra correta era {palavra_sorteada}.')
        break

    fH.inserir_score('score.txt', nome, score)