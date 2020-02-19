import os

class vsJogador():
    def __init__(self):

        self.placar = {'X':0, 'O':0}
        self.jogoPrincipal = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.coordenadas = {1:'00', 2:'01', 3:'02',
                            4:'10', 5:'11', 6:'12',
                            7:'20', 8:'21', 9:'22'}

    #apaga o console e mostra o cabecalho do jogo na tela
    def cabecalho(self):
        os.system('cls')
        print('*** JOGO DA VELHA - PYTHON 3 - V1.0 ***')
        print('***    Modo de Jogo: vsJogador      ***')

    #inicia ou não uma partida
    def iniciaJogo(self):
        self.cabecalho()

        novoJogo = True
        novoJogo = input('\nQuer iniciar um Jogo da Velha (S/n)? ')
        if novoJogo in 'simSimSIM': return True

        return False

    #reseta tabuleiro do jogo
    def resetaJogoPrincipal(self):
        self.jogoPrincipal = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    #finaliza o jogo mostrando o vencedor, alterando e mostrando o placar
    def finalizaJogo(self, simbolo):
        if simbolo:
            self.placar[simbolo] += 1
            self.mostraJogoPrincipal()
            print('O Jogo Acabou! %c Ganhou!!!' %simbolo)
        else:
            self.mostraJogoPrincipal()
            print('O Jogo Acabou! Deu Velha!')

        self.resetaJogoPrincipal()

        print('Placar: X (%d) | O (%d)' %(self.placar['X'], self.placar['O']))

    #mostra o tabuleiro do Jogo em Execução
    def mostraJogoPrincipal(self):
        self.cabecalho()

        print()
        for linha, col1, col2, col3 in zip(self.jogoPrincipal, range(1,8,3), range(2,9,3), range(3,10,3)):
            print('| %c | %c | %c |' %(linha[0], linha[1], linha[2]), end="\t\t")
            print('| %d | %d | %d |' %(col1, col2, col3))
        print()

    #exerce a jogada para o símbolo da rodada
    def jogada(self, simbolo):
        numJogada = 0
        while numJogada < 1 or numJogada > 9:
            numJogada = int(input('Próxima Jogada de %c: ' %simbolo))
        
        self.jogoPrincipal[int(self.coordenadas[numJogada][0])][int(self.coordenadas[numJogada][1])] = simbolo

    def comparaVencedor(self, simbolo):
        #compara linhas
        if (self.jogoPrincipal[0][0] == self.jogoPrincipal[0][1] == self.jogoPrincipal[0][2] == simbolo) or (self.jogoPrincipal[1][0] == self.jogoPrincipal[1][1] == self.jogoPrincipal[1][2] == simbolo) or (self.jogoPrincipal[2][0] == self.jogoPrincipal[2][1] == self.jogoPrincipal[2][2] == simbolo):
            self.finalizaJogo(simbolo)
            return True
        #compara colunas
        elif (self.jogoPrincipal[0][0] == self.jogoPrincipal[1][0] == self.jogoPrincipal[2][0] == simbolo) or (self.jogoPrincipal[0][1] == self.jogoPrincipal[1][1] == self.jogoPrincipal[2][1] == simbolo) or (self.jogoPrincipal[0][2] == self.jogoPrincipal[1][2] == self.jogoPrincipal[2][2] == simbolo):
            self.finalizaJogo(simbolo)
            return True
        #compara diagonais
        elif (self.jogoPrincipal[0][0] == self.jogoPrincipal[1][1] == self.jogoPrincipal[2][2] == simbolo) or (self.jogoPrincipal[2][0] == self.jogoPrincipal[1][1] == self.jogoPrincipal[0][2] == simbolo):
            self.finalizaJogo(simbolo)
            return True

        return False

    #execução do jogo
    def execucaoJogoPrincipal(self):
        while self.iniciaJogo():
            situacao = False

            for simbolo in ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']:
                self.mostraJogoPrincipal()
                self.jogada(simbolo)
                situacao = self.comparaVencedor(simbolo)
                if situacao:
                    break

            if not situacao:
                self.finalizaJogo(False)

            input()