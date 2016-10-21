from socket import *
jogada=input("Digite o lugar onde vai jogar")
cliente_velha = socket(AF_INET, SOCK_STREAM)
ip_server= '192.168.1.131'
porta=50012
servidor=(ip_server, porta)
cliente_velha.connect(servidor)
cliente_velha.send(jogada.encode())
data=(cliente_velha.recv(4096))
resposta=data.decode('ascii')
print (reposta)
