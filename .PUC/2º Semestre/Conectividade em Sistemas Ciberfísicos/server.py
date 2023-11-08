import socket
import threading


def recebedados(cliente):
#LOOP PARA RECEBER BANCO DE DADOS 
    while True: 
        try:
            mensagem = conn.recv(1024).decode() #ACEITA 1024 BYTES
            mensagemnome = nome + ': ' + mensagem
            print(mensagemnome)
        except:
            print('Ocorreu algum erro ao receber as mensagens... Fechando conexao')
            conm.close()
            break
    
    


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
print(f"O servidor {HOST}:{PORT} está ativo e aguardando conexões...")

#FUNÇÃO QUE É "ACESSA" PELO CONNECT DO CLIENTE, RETORNA 2 PARAMETROS 
#CON É O SOCKET DO CLIENTE E O ENDER É O ENDEREÇO 
#ESSE É O PONTO QUE CONECTAMOS O CLIENTE 
#PARA TERMOS VÁRIOS, PRECISAMOS DE UM LOOP INFINITO


conn, ender = sock.accept()
print("Conexão em ", ender)


while True:
    try:
        conm, ender = sock.accept()
        #ENDER[0] = IP ENDER[1] = PORTA
        nome = conm.recv(50).decode() #RECEBER DADOS EM UTF-8
        print(f'Conexâo com sucesso com {nome} - {ender[0]}:{ender[1]}')
    except:
        print('Algum erro de conexâo ocorreu... tentando novamente')
        continue
    threadCliente = threading.Thread(target=recebedados , args=[conm])
    threadCliente.start()




        
        