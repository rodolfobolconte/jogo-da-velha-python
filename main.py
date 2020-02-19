import os
from vsJogador import *


jogoPrincipal = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
coordenadas = {1:'00', 2:'01', 3:'02',
               4:'10', 5:'11', 6:'12',
               7:'20', 8:'21', 9:'22'}
placar = {'X':0, 'O':0}

#reseta tabuleiro do jogo
def resetaJogoPrincipal():
    global jogoPrincipal
    
    jogoPrincipal = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#apaga o console e mostra o cabecalho do jogo na tela
def cabecalho():
    os.system('cls')
    print('*** JOGO DA VELHA - PYTHON 3 - v1.0 ***')

#mostra o tabuleiro do Jogo em Execução
def mostraJogoPrincipal():
    cabecalho()

    print()
    for linha, col1, col2, col3 in zip(jogoPrincipal, range(1,8,3), range(2,9,3), range(3,10,3)):
        print('| %c | %c | %c |' %(linha[0], linha[1], linha[2]), end="\t\t")
        print('| %d | %d | %d |' %(col1, col2, col3))
    print()

#exerce a jogada para o símbolo da rodada
def jogada(simbolo):
    numJogada = 0
    while numJogada < 1 or numJogada > 9:
        numJogada = int(input('Próxima Jogada de %c: ' %simbolo))
    
    jogoPrincipal[int(coordenadas[numJogada][0])][int(coordenadas[numJogada][1])] = simbolo

#finaliza o jogo mostrando o vencedor, alterando e mostrando o placar
def finalizaJogo(simbolo):
    if simbolo:
        placar[simbolo] += 1
        mostraJogoPrincipal()
        print('O Jogo Acabou! %c Ganhou!!!' %simbolo)
    else:
        mostraJogoPrincipal()
        print('O Jogo Acabou! Deu Velha!')

    resetaJogoPrincipal()

    print('Placar: X (%d) | O (%d)' %(placar['X'], placar['O']))

#inicia ou não uma partida
def iniciaJogo():
    cabecalho()

    novoJogo = True
    novoJogo = input('\nQuer iniciar um Jogo da Velha (S/n)? ')
    if novoJogo in 'simSimSIM': return True

    return False


#compara as jogadas se teve algum vencedor
def comparaVencedor(simbolo):
    #compara linhas
    if (jogoPrincipal[0][0] == jogoPrincipal[0][1] == jogoPrincipal[0][2] == simbolo) or (jogoPrincipal[1][0] == jogoPrincipal[1][1] == jogoPrincipal[1][2] == simbolo) or (jogoPrincipal[2][0] == jogoPrincipal[2][1] == jogoPrincipal[2][2] == simbolo):
        finalizaJogo(simbolo)
        return True
    #compara colunas
    elif (jogoPrincipal[0][0] == jogoPrincipal[1][0] == jogoPrincipal[2][0] == simbolo) or (jogoPrincipal[0][1] == jogoPrincipal[1][1] == jogoPrincipal[2][1] == simbolo) or (jogoPrincipal[0][2] == jogoPrincipal[1][2] == jogoPrincipal[2][2] == simbolo):
        finalizaJogo(simbolo)
        return True
    #compara diagonais
    elif (jogoPrincipal[0][0] == jogoPrincipal[1][1] == jogoPrincipal[2][2] == simbolo) or (jogoPrincipal[2][0] == jogoPrincipal[1][1] == jogoPrincipal[0][2] == simbolo):
        finalizaJogo(simbolo)
        return True

    return False

"""while iniciaJogo():
    situacao = False

    for simbolo in ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']:
        mostraJogoPrincipal()
        jogada(simbolo)
        situacao = comparaVencedor(simbolo)
        if situacao:
            break

    if not situacao:
        finalizaJogo(False)

    input()"""

cabecalho()

modoDeJogo = int(input('\nEscolha o método de jogo (1- vsJogador | 2- vsComputador): '))

if modoDeJogo == 1:
    novoJogo = vsJogador()
    novoJogo.execucaoJogoPrincipal()