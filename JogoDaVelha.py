jogo=[['','',''],['','',''],['','','']]

def vezdeX():
    jog=input('\nOnde jogar X? ')

    while len(jog)!=2 or (jog[0]!='0' and jog[0]!='1' and jog[0]!='2') or (jog[1]!='0' and jog[1]!='1' and jog[1]!='2'):
        jog=input('Posição Inválida. Onde jogar X? ')

    i=int(jog[0]) ; j=int(jog[1])

    while jogo[i][j]!=' ':
        jog=input('Jogada Não Permitida. Onde jogar X? ')
        i=int(jog[0]) ; j = int(jog[1])

    jogo[i][j]='X'

def vezdeO():
    jog = input('\nOnde jogar O? ')

    while len(jog)!=2 or (jog[0]!='0' and jog[0]!='1' and jog[0]!='2') or (jog[1]!='0' and jog[1]!='1' and jog[1]!='2'):
        jog = input('Posição Inválida. Onde jogar O? ')

    i = int(jog[0]) ; j = int(jog[1])

    while jogo[i][j]!=' ':
        jog=input('Jogada Não Permitida. Onde jogar O? ')
        i=int(jog[0]) ; j=int(jog[1])

    jogo[i][j]='O'
