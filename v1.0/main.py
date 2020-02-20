import os
from vsJogador import *
from vsComputador import *

#apaga o console e mostra o cabecalho do jogo na tela
def cabecalho():
    os.system('cls')
    print('*** JOGO DA VELHA - PYTHON 3 - v1.0 ***')

cabecalho()

modoDeJogo = input('\nEscolha o método de jogo (1- vsJogador | 2- vsComputador | s- Sair): ')

while modoDeJogo not in 'SairsairSAIR':
    if modoDeJogo == '1':
        novoJogo = vsJogador()
        novoJogo.execucaoJogoPrincipal()
    elif modoDeJogo == '2':
        novoJogo = vsComputador()
        novoJogo.execucaoJogoPrincipal()

    cabecalho
    modoDeJogo = input('\nEscolha o método de jogo (1- vsJogador | 2- vsComputador | s- Sair): ')