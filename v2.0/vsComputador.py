import os
import random

class Jogador:
    def __init__(self):
        self.tabuleiro = [' '] * 9
        self.jogadores = {'1':'X', '2':'O'}
        self.placar = {'1':0, '2':0, 'Velha':0}


    def iniciarJogo(self):
        self.tabuleiro = [' '] * 9

        simboloJogador = ' '
        
        while simboloJogador not in 'XO':
            simboloJogador = input('Escolha o símbolo do Jogador 1 (X ou O): ')
        
        if simboloJogador == 'O': self.jogadores['1'] = 'O' ; self.jogadores['2'] = 'X'

    def cabecalhoJogo(self):
        os.system('cls')
        print('********   JOGO DA VELHA - v2.0   *********')

    def imprimirJogo(self):
        print('***********   Modo vsJogador   ************\n')
        print('|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|\t|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|')
        print('|  %c  |  %c  |  %c  |\t|  1  |  2  |  3  |' %(self.tabuleiro[0], self.tabuleiro[1], self.tabuleiro[2]))
        print('|_____|_____|_____|\t|_____|_____|_____|')
        print('|     |     |     |\t|     |     |     |')
        print('|  %c  |  %c  |  %c  |\t|  4  |  5  |  6  |' %(self.tabuleiro[3], self.tabuleiro[4], self.tabuleiro[5]))
        print('|_____|_____|_____|\t|_____|_____|_____|')
        print('|     |     |     |\t|     |     |     |')
        print('|  %c  |  %c  |  %c  |\t|  7  |  8  |  9  |' %(self.tabuleiro[6], self.tabuleiro[7], self.tabuleiro[8]))
        print('|_____|_____|_____|\t|_____|_____|_____|')

    def verificaJogada(self, numJogada):
        if (numJogada < 1 or numJogada > 9):
            return False

        elif self.tabuleiro[numJogada - 1] not in ' ':
            return False

        return True

    def jogada(self, jogador):
        numJogada = int(input('\nMovimento do Jogador %c: ' %jogador))

        while not self.verificaJogada(numJogada):
            self.cabecalhoJogo()
            self.imprimirJogo()
            numJogada = int(input('\nMovimento Não Permitido. Novo Movimento do Jogador %c: ' %jogador))
        
        self.tabuleiro[numJogada - 1] = self.jogadores[jogador]

    def comparaVencedor(self, vezJogador):
        simbolo = self.jogadores[vezJogador]

                #compara linhas
        return ((self.tabuleiro[0] == self.tabuleiro[1] == self.tabuleiro[2] == simbolo) or
                (self.tabuleiro[3] == self.tabuleiro[4] == self.tabuleiro[5] == simbolo) or
                (self.tabuleiro[6] == self.tabuleiro[7] == self.tabuleiro[8] == simbolo) or
                #compara colunas
                (self.tabuleiro[0] == self.tabuleiro[3] == self.tabuleiro[6] == simbolo) or 
                (self.tabuleiro[1] == self.tabuleiro[4] == self.tabuleiro[7] == simbolo) or 
                (self.tabuleiro[2] == self.tabuleiro[5] == self.tabuleiro[8] == simbolo) or
                #compara diagonais
                (self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] == simbolo) or
                (self.tabuleiro[6] == self.tabuleiro[4] == self.tabuleiro[2] == simbolo))

    def computaVencedor(self, resultado):
        if resultado in 'Velha':
            print('\nAcabou! O Jogo deu Velha!')
            self.placar[resultado] += 1
        else:
            print('\nAcabou! O Jogador %c venceu o jogo!!!' %resultado)
            self.placar[resultado] += 1

        print('Placar: Jogador 1 (%d) x (%d) Jogador 2 | Velhas (%d)' %(self.placar['1'], self.placar['2'], self.placar['Velha']))

    def execucaoVsJogador(self):
        iniciarJogo()

        velha = True

        for vezJogador in ['1', '2', '1', '2', '1', '2', '1', '2', '1']:
            self.cabecalhoJogo()
            self.imprimirJogo()
            
            self.jogada(vezJogador)

            if self.comparaVencedor(vezJogador):
                velha = False
                break

        self.cabecalhoJogo()
        self.imprimirJogo()

        if velha:
            self.computaVencedor('Velha')
        else:
            self.computaVencedor(vezJogador)

    def jogadaComputador(self):
        if self.tabuleiro


modoDeJogo = input('Escolha o Modo de Jogo (1- vsJogador | 2- vsComputador | s- Sair): ')
while modoDeJogo not in 's':
    if modoDeJogo in '1':
        vsJogador = Jogador()
        vsJogador.execucaoVsJogador()

    modoDeJogo = input('Escolha o Modo de Jogo (1- vsJogador | 2- vsComputador | s- Sair): ')