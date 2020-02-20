import os

tabuleiro = [' '] * 9
jogadores = {}
placar = {'1':0, '2':0, 'Velha':0}

def iniciarJogo():
    simboloJogador = ' '
    
    while simboloJogador not in 'XO':
        simboloJogador = input('Escolha o símbolo do Jogador 1 (X ou O): ')
    
    if simboloJogador == 'X': jogadores['1'] = 'X' ; jogadores['2'] = 'O'
    else: jogadores['1'] = 'O' ; jogadores['2'] = 'X'

def cabecalhoJogo():
    os.system('cls')
    print('********   JOGO DA VELHA - v2.0   *********')

def imprimirJogo():
    print('***********   Modo vsJogador   ************\n')
    print('|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|\t|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|')
    print('|  %c  |  %c  |  %c  |\t|  1  |  2  |  3  |' %(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print('|_____|_____|_____|\t|_____|_____|_____|')
    print('|     |     |     |\t|     |     |     |')
    print('|  %c  |  %c  |  %c  |\t|  4  |  5  |  6  |' %(tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print('|_____|_____|_____|\t|_____|_____|_____|')
    print('|     |     |     |\t|     |     |     |')
    print('|  %c  |  %c  |  %c  |\t|  7  |  8  |  9  |' %(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print('|_____|_____|_____|\t|_____|_____|_____|')

def verificaJogada(numJogada):
    if (numJogada < 1 or numJogada > 9):
        return False

    elif tabuleiro[numJogada - 1] not in ' ':
        return False

    return True

def jogada(jogador):
    numJogada = int(input('Movimento do Jogador %c: ' %jogador))

    while not verificaJogada(numJogada):
        numJogada = int(input('Movimento do Jogador %c: ' %jogador))
    
    tabuleiro[numJogada - 1] = jogadores[jogador]

def comparaVencedor(vezJogador):
    simbolo = jogadores[vezJogador]

    #compara linhas
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == simbolo) or (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == simbolo) or (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == simbolo):
        return True
    #compara colunas
    elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == simbolo) or (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo) or (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo):
        return True
    #compara diagonais
    elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == simbolo) or (tabuleiro[6] == tabuleiro[4] == tabuleiro[2] == simbolo):
        return True

    return False

def computaVencedor(resultado):
    if resultado in 'Velha':
        print('\nAcabou! O Jogo deu Velha!')
        placar[resultado] += 1
    else:
        print('\nAcabou! O Jogador %c venceu o jogo!!!' %resultado)
        placar[resultado] += 1

    print('Placar: Jogador 1 (%d) x (%d) Jogador 2 | Velhas (%d)' %(placar['1'], placar['2'], placar['Velha']))





modoDeJogo = input('Escolha o Modo de Jogo (1- vsJogador | 2- vsComputador | s- Sair): ')
while modoDeJogo not in 's':
    if modoDeJogo in '1':
        iniciarJogo()

        velha = True

        for vezJogador in ['1', '2', '1', '2', '1', '2', '1', '2', '1']:
            cabecalhoJogo()
            imprimirJogo()
            
            jogada(vezJogador)

            if comparaVencedor(vezJogador):
                velha = False
                break

        cabecalhoJogo()
        imprimirJogo()

        if velha:
            computaVencedor('Velha')
        else:
            computaVencedor(vezJogador)

    modoDeJogo = input('Escolha o Modo de Jogo (1- vsJogador | 2- vsComputador | s- Sair): ')