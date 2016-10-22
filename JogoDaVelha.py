from random import randint
from random import choice

jogo=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def imprime():
    print()
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(jogo[i][j], end=' | ')

        print('    | ', end='')
        for k in range(3):
            print('%i%i'%(i,k), end=' | ')

        print()

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

def compara(jog):
    cont=0
    #Compara horizontal
    for i in range(3):
        for j in range(3):
            if jogo[i][j]==jog:
                cont+=1
        if cont==3: print('\n%c Ganhou!!!'%jog) ; cont=0 ; return 1
        cont=0

    #Compara vertical
    for i in range(3):
        for j in range(3):
            if jogo[j][i]==jog:
                cont+=1
        if cont==3: print('\n%c Ganhou!!!'%jog) ; cont=0 ; return 1
        cont=0

    #Compara diagonal
    if jogo[0][0]==jog and jogo[1][1]==jog and jogo[2][2]==jog: print('\n%c Ganhou!!!'%jog) ; return 1
    elif jogo[2][0]==jog and jogo[1][1]==jog and jogo[0][2]==jog: print('\n%c Ganhou!!!'%jog) ; return 1

    return 0

def IA(marcaPlayer, marcaPC):
    cont = 0
    print("\nComputador jogou em:")
    if (((jogo[0][1] == marcaPC and jogo[2][1] == marcaPC) or
             (jogo[1][0] == marcaPC and jogo[1][2] == marcaPC) or
             (jogo[0][0] == marcaPC and jogo[2][2] == marcaPC) or
             (jogo[2][0] == marcaPC and jogo[0][2] == marcaPC)) and (jogo[1][1] == " ")):
        jogo[1][1] = marcaPC

    elif (((jogo[0][0] == marcaPC and jogo[0][1] == marcaPC) or
               (jogo[2][0] == marcaPC and jogo[1][1] == marcaPC) or
               (jogo[1][2] == marcaPC and jogo[2][2] == marcaPC)) and (jogo[0][2] == " ")):
        jogo[0][2] = marcaPC

    elif (((jogo[0][1] == marcaPC and jogo[0][2] == marcaPC) or
               (jogo[2][0] == marcaPC and jogo[1][0] == marcaPC) or
               (jogo[1][2] == marcaPC and jogo[1][1] == marcaPC)) and (jogo[0][0] == " ")):
        jogo[0][0] = marcaPC

    elif (((jogo[0][0] == marcaPC and jogo[1][0] == marcaPC) or
               (jogo[2][1] == marcaPC and jogo[2][2] == marcaPC) or
               (jogo[1][1] == marcaPC and jogo[0][2] == marcaPC)) and (jogo[2][0] == " ")):
        jogo[2][0] = marcaPC

    elif (((jogo[0][2] == marcaPC and jogo[1][2] == marcaPC) or
               (jogo[2][1] == marcaPC and jogo[2][0] == marcaPC) or
               (jogo[1][1] == marcaPC and jogo[0][0] == marcaPC)) and (jogo[2][2] == " ")):
        jogo[2][2] = marcaPC

    elif (((jogo[0][2] == marcaPC and jogo[2][2] == marcaPC) or
               (jogo[1][1] == marcaPC and jogo[1][0] == marcaPC)) and (jogo[1][2] == " ")):
        jogo[1][2] = marcaPC

    elif (((jogo[0][1] == marcaPC and jogo[1][1] == marcaPC) or
               (jogo[2][0] == marcaPC and jogo[2][2] == marcaPC)) and (jogo[2][1] == " ")):
        jogo[2][1] = marcaPC

    elif (((jogo[0][0] == marcaPC and jogo[0][2] == marcaPC) or
               (jogo[1][1] == marcaPC and jogo[2][1] == marcaPC)) and (jogo[0][1] == " ")):
        jogo[0][1] = marcaPC

    elif (((jogo[0][0] == marcaPC and jogo[2][0] == marcaPC) or
               (jogo[1][1] == marcaPC and jogo[1][2] == marcaPC)) and (jogo[1][0] == " ")):
        jogo[1][0] = marcaPC
        # caso contrario avalia se o adversario pode bater e tenta impedir
    else:
        if (((jogo[0][1] == marcaPlayer and jogo[2][1] == marcaPlayer) or
                 (jogo[1][0] == marcaPlayer and jogo[1][2] == marcaPlayer) or
                 (jogo[0][0] == marcaPlayer and jogo[2][2] == marcaPlayer) or
                 (jogo[2][0] == marcaPlayer and jogo[0][2] == marcaPlayer)) and (jogo[1][1] == " ")):
            jogo[1][1] = marcaPC

        elif (((jogo[0][0] == marcaPlayer and jogo[0][1] == marcaPlayer) or
                   (jogo[2][0] == marcaPlayer and jogo[1][1] == marcaPlayer) or
                   (jogo[1][2] == marcaPlayer and jogo[2][2] == marcaPlayer)) and (jogo[0][2] == " ")):
            jogo[0][2] = marcaPC

        elif (((jogo[0][1] == marcaPlayer and jogo[0][2] == marcaPlayer) or
                   (jogo[2][0] == marcaPlayer and jogo[1][0] == marcaPlayer) or
                   (jogo[1][2] == marcaPlayer and jogo[1][1] == marcaPlayer)) and (jogo[0][0] == " ")):
            jogo[0][0] = marcaPC

        elif (((jogo[0][0] == marcaPlayer and jogo[1][0] == marcaPlayer) or
                   (jogo[2][1] == marcaPlayer and jogo[2][2] == marcaPlayer) or
                   (jogo[1][1] == marcaPlayer and jogo[0][2] == marcaPlayer)) and (jogo[2][0] == " ")):
            jogo[2][0] = marcaPC

        elif (((jogo[0][2] == marcaPlayer and jogo[1][2] == marcaPlayer) or
                   (jogo[2][1] == marcaPlayer and jogo[2][0] == marcaPlayer) or
                   (jogo[1][1] == marcaPlayer and jogo[0][0] == marcaPlayer)) and (jogo[2][2] == " ")):
            jogo[2][2] = marcaPC

        elif (((jogo[0][2] == marcaPlayer and jogo[2][2] == marcaPlayer) or
                   (jogo[1][1] == marcaPlayer and jogo[1][0] == marcaPlayer)) and (jogo[1][2] == " ")):
            jogo[1][2] = marcaPC

        elif (((jogo[0][1] == marcaPlayer and jogo[1][1] == marcaPlayer) or
                   (jogo[2][0] == marcaPlayer and jogo[2][2] == marcaPlayer)) and (jogo[2][1] == " ")):
            jogo[2][1] = marcaPC

        elif (((jogo[0][0] == marcaPlayer and jogo[0][2] == marcaPlayer) or
                   (jogo[1][1] == marcaPlayer and jogo[2][1] == marcaPlayer)) and (jogo[0][1] == " ")):
            jogo[0][1] = marcaPC

        elif (((jogo[0][0] == marcaPlayer and jogo[2][0] == marcaPlayer) or
                   (jogo[1][1] == marcaPlayer and jogo[1][2] == marcaPlayer)) and (jogo[1][0] == " ")):
            jogo[1][0] = marcaPC

        else:
            l=randint(0, 2)
            c=randint(0, 2)
            while jogo[l][c] != ' ':
                l = randint(0, 2)
                c = randint(0, 2)

            jogo[l][c]=marcaPC

    return 0