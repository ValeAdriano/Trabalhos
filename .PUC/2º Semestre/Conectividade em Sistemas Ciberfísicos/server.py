import socket


#criação do socket e das informações do servidor
HOST = "127.0.0.1"
PORT = 9991

#IPV4 É O PARAMETRO AF_INET
#TCP É O PARAMETRO SOCK_STREM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))
#127.0.0.1
#O SERVIDOR ESTÁ ESCUTANDO...
sock.listen()
print(f"O servidor {HOST}{PORT} está ativo e aguardando conexões...")

#FUNÇÃO QUE É "ACESSA" PELO CONNECT DO CLIENTE, RETORNA 2 PARAMETROS 
#CON É O SOCKET DO CLIENTE E O ENDER É O ENDEREÇO 
#ESSE É O PONTO QUE CONECTAMOS O CLIENTE 
#PARA TERMOS VÁRIOS, PRECISAMOS DE UM LOOP INFINITO


conn, ender = sock.accept()
print("Conexão em ", ender)

#LOOP PARA RECEBER BANCO DE DADOS 
while True: 
    dados = conn.recv(1024) #ACEITA 1024 BYTES
    if not dados:
        print("Fechando conexão...")
        conn.close()
        break
    conn.sendall(dados)
    
    