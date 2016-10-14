#sites pesquisados para poder utilizar socket
#http://wiki.python.org.br/SocketBasico
#http://www.scriptbrasil.com.br/forum/topic/96896-socket-em-python-como-interagir-enfim-resolvido/
#Primeira função para utilizar o socket que nesse caso é cliente jogo da velha
import socket
HOST = '192.168.1.10'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
cliente_velha = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg <> '\x18':
    cliente_velha.sendto (msg, dest)
    msg = raw_input()
cliente_velha.close()
