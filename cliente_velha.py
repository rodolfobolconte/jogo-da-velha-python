#sites pesquisados para poder utilizar socket
#http://wiki.python.org.br/SocketBasico
#http://www.scriptbrasil.com.br/forum/topic/96896-socket-em-python-como-interagir-enfim-resolvido/
#Primeira função para utilizar o socket que nesse caso é cliente jogo da velha
import socket
ip_maquina=input("Digite o endereço ip da maquina")
PORT = 5000            # Porta que sera utilizada para acessar o servidor, pode ser alterada para outro valor
cliente_velha = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print ("Para sair use CTRL+X\n")
#essa variavel "msg" é a mensagem que vai ser enviada, ou seja a posição 
#que vai ser jogado, então qualquer coisa tem que modificar ou só atruibir 
#para msg o valor da outra variavel e retirar o raw_input
msg = raw_input()
while msg <> ("\x18"):
    cliente_velha.sendto (msg, dest)
    msg = raw_input()
cliente_velha.close()
