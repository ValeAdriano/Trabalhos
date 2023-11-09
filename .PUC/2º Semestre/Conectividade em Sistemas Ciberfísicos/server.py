import socket
import threading
import os

def limpaTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def recebeDados(conn,ender):
    #recebimento do nome do cliente que teve a conexão aceita
    try:
        nome = conn.recv(50).decode() #50 é o tamanho do buffer
        print(f"Conectado com {nome}, IP: {ender[0]}, PORTA: {ender[1]}")
    except:
        print("Ocorreu um erro durante o recebimento do nome. A conexão será encerrada")
        return
    while True:
        try:
            mensagem = conn.recv(1024).decode()
            mensagemNome = nome + " >> " + mensagem
            print(mensagemNome)
            #estamos fazendo um broadcast via aplicação (#todo: criar função broadcast)
            try:
                for cliente in lista_cliente:
                    cliente.sendall(mensagemNome.encode())
            except:
                print("Ocorreu algum erro no envio dos dados...")
                return
        except:
            print("Ocorreu algum erro na recepção dos dados, encerrando conexão.")
            break

HOST = 'localhost' #127.0.0.1
PORT = 9999
limpaTerminal()
lista_cliente = []
#inicializar o socket com seus parâmetros básicos (IPv4 e TCP)
#AF_INET É IPV4
#SOCK_STREAM É TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#PRECISAMOS VINCULAR O SOCKET SERVIDOR: ENDEREÇO IP : PORTA -> BIND
#LOCALHOST:9999 COMO SERVIDOR
sock.bind((HOST,PORT))

#AGORA O SERVIDOR COMEÇA A ESCUTAR CONEXÕES
sock.listen() #abre a porta
print(f"O Servidor {HOST}:{PORT} está aguardando conexões")

while True:
    #ACEITAMOS A CONEXÃO de vários clientes
    #conn é o socket do cliente
    #ender é a porta do cliente
    try:
        conn, ender = sock.accept()
        #adicionado cliente a lista de clientes
        lista_cliente.append(conn)
    except:
        print('Ocorreu um erro durante o ACCEPT() na conexão com um novo usuário')
        continue
    
    
    #LOOP INFINITO PARA RECEBIMENTO DE DADOS: VAI PARA A FUNÇÃO QUE SERÁ EXECUTADA PELA THREAD
    threadCliente = threading.Thread(target=recebeDados, args=[conn,ender])
    threadCliente.start()
    
  
     
   

