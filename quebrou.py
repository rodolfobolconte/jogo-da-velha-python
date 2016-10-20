from socket import *
ip='192.168.1.131'
porta=50012
tcp_cliente = socket(AF_INET, SOCK_STREAM)
destino=(ip,porta)
tcp_cliente.bind(destino)
tcp_cliente.connect(destino)
print ("Para sair use CTRL+X")
msg = input("Digite o valor")
tcp_cliente.send(msg)
data=tcp_cliente.recv(1024)
print ("Foi recebido : ",data)
tcp.close()
