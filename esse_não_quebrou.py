from socket import *
HOST = '192.168.1.131'              # Endereco IP do Servidor
PORT = 50012            # Porta que o Servidor esta
tcp_serv = socket(AF_INET, SOCK_STREAM)
orig = (HOST, PORT)
tcp_serv.bind(orig)
tcp_serv.listen(1)
print("Esperando iniciar a conexao")
data_to_send = "dados do servidor"
data_received=""
tcp_cliente, address = tcp_serv.accept()
print("endereço",address)
