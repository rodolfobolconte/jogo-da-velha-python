from socket import *
ip_da_maquina_servidor='192.168.25.28' # Endereco IP do Servidor, deve ser setado caso esteja em redes diferentes, ou como localhost se estiver na rede local ou seja mesma maquina nesse caso
porta_de_conexao=49250  # Porta que o Servidor esta conetando
servidor_velha = socket(socket.AF_INET, socket.SOCK_DGRAM) # serve para criar um objeto socket tcp 
servidor_velha.bind((ip_da_maquina_servidor,porta_de_conexao)) # com esse comando liga-se o servidor ao número da porta
servidor_velha.listen(1) # serve para definir o numero maximo de conexoes que nesse caso so uma
while True:
    connection, address=servidor_velha.accept()
    print "existe uma conexao com ", address
    while True:
        data=connection.recv(1024)
        print date
        if not data: break
        connection.send("Recebi isso :"+data)
    connection.close()
