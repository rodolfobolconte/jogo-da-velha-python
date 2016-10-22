from socket import *
from time import time, ctime

HOST = '192.168.0.104'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while 1:
    print ("Aguardando conexao...")
    tcpClisock, addr = tcpSerSock.accept()
    print ("...conexao de :"), addr
    while 1:
    	data = tcpClisock.recv(BUFSIZ)
    	print ("[+] %s") % (data)
    	mensagem=raw_input('Mensagem do servidor :')
    	if data=="exit": 
    		exit
    	tcpClisock.send(mensagem)
tcpClisock.close()
exit
tcpClicksock.close()


