import socket

#PRECISAMOS NOS CONECTAR NO SERVIDOR 
HOST = '127.0.0.1' #LOCAL HOST
PORT = 9991

sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CLIENTE SOLOCITA A CONEXAO COM O SERVIDOR 
sock_cliente.connect((HOST, PORT))
#CLIENTE ENVIA DADOS PARA O SERVIDOR 
sock_cliente.sendall(str.encode("Ola eu sou o cliente 1 !!!"))

dados = socket_cliente.recv(1024)
print('Menssagem recebida para teste: ')
print(dados.decode())
