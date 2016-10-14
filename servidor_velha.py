import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
servidor_velha = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
servidor_velha.bind(orig)
while True:
    msg, cliente = servidor_velha.recvfrom(1024)
    print cliente, msg
servidor_velha.close()
