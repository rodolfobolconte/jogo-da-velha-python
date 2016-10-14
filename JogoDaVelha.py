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

comeco='xo' ; comeco=choice(comeco)

if comeco=='x':
    for i in range(4):
        imprime() ; vezdeX()
        if compara('X') == 1:
            break
        imprime() ; vezdeO()
        if compara('O')==1:
            break
        if i==3:
            imprime() ; vezdeX()
            if compara('X')==0:
            	imprime()
            	print('\nVelha!!!')

else:
    for i in range(4):
        imprime() ; vezdeO()
        if compara('O')==1:
            break
        imprime() ; vezdeX()
        if compara('X')==1:
            break
        if i==3:
            imprime() ; vezdeO()
            if compara('O')==0:
            	imprime()
            	print('\nVelha!!!')
