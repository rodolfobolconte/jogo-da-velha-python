from socket import * 


HOST = '192.168.0.104' 
PORT = 21567 
BUFSIZ = 1024 
ADDR = (HOST, PORT) 

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR) 

while 1: 
	data = raw_input("CLIENT > ")
	print ("[CLIENT] vc digitou %s") % (data) 
	if not data: 
		break
	tcpCliSock.send(data) 
	data = tcpCliSock.recv(1024) 
	if not data: 
		break 
	print (data) 

tcpCliSock.close()
