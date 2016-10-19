#sites pesquisados para poder utilizar socket
#http://wiki.python.org.br/SocketBasico
#http://www.scriptbrasil.com.br/forum/topic/96896-socket-em-python-como-interagir-enfim-resolvido/
#Primeira função para utilizar o socket que nesse caso é cliente jogo da velha
from socket import *
ip_servidor=input("Digite o endereço ip da maquina servidor, se for uma conexão local so precisa digitar logalhost")
porta_de_conexao=49250        # Porta que sera utilizada para acessar o servidor, pode ser alterada para outro valor
servidor_velha=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_velha.connect((ip_servidor,porta_de_conexao))
jogada= #Essa variavel vai receber o local onde foi feito a jogada, então que que a cada jogada essa variavel receber a nova jogada
for line in jogada:
    servidor_velha.send(jogada) #isso é pra enviar a jogada para o servidor.
    data=servidor_velha.recv(1024) # recebe o retorno da mensagem, que nesse caso é bom configurar para ser a jogada da outra maquina
    print "A jogada do outro jogador foi na :",repr(data)
servidor_velha.close()

