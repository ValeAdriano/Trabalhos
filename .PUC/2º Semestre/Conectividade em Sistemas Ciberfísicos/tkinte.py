import tkinter as tk
import socket
import threading 

#INFORMAÇÕES DO SERVIDOR
HOST = "127.0.0.1"
PORT = 9999

#função de recebimento de dados do cliente
def recebeDados(conn, chat):
    try:
        while True:
            mensagem = conn.recv(1024).decode()
            chat.insert(tk.END, mensagem)
            chat.see(tk.END)
    except:
        print("Erro no recebimento de mensagens do servidor...")
        return

#função para enviar mensagem
def enviaMensagem(event=None):
    mensagem = minhaMensagem.get()
    minhaMensagem.set("") #limpa a caixa de mensagem
    sock.sendall(str.encode(mensagem))
    if mensagem == ('/kill'):
        sock.close()
        root.quit()

#função para limpar a tela
def limpaTela():
    chat.delete('1.0', tk.END)

#função para sair do chat
def sairDoChat():
    mensagem = "/kill"
    sock.sendall(str.encode(mensagem))
    sock.close()
    root.quit()

#COMO A CONEXÃO É TCP PRECISAMOS DE UM CONNECT
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT)) #CONNECT ACENDE O ACCEPT DO SERVIDOR

#enviando nome para o servidor
nome = input("Informe o seu nome: ")
sock.sendall(str.encode(nome))

#criando a janela
root = tk.Tk()
root.title("Chat")
root.geometry("800x600")

#criando a tela de entrada
telaDeEntrada = tk.Frame(root, bg="red", width=400, height=600)
telaDeEntrada.pack(side=tk.LEFT, fill=tk.BOTH)

#criando o label de nome
labelDeNome = tk.Label(telaDeEntrada, text="Nome: " + nome, font=("Helvetica", 16), bg="red", fg="white")
labelDeNome.pack(pady=10)

#criando a tela de chat
telaDeChat = tk.Frame(root, bg="gray", width=400, height=600)
telaDeChat.pack(side=tk.RIGHT, fill=tk.BOTH)

#criando a caixa de chat
chat = tk.Text(telaDeChat, height=20, width=50)
chat.pack(side=tk.TOP, padx=10, pady=10)

#criando a caixa de mensagem
minhaMensagem = tk.StringVar()
caixaDeMensagem = tk.Entry(telaDeChat, textvariable=minhaMensagem, width=50)
caixaDeMensagem.bind("<Return>", enviaMensagem)
caixaDeMensagem.pack(side=tk.LEFT, padx=10, pady=10)

#criando o botão de envio
botaoDeEnvio = tk.Button(telaDeChat, text="Enviar", command=enviaMensagem)
botaoDeEnvio.pack(side=tk.LEFT, padx=10, pady=10)

#criando o botão de limpar tela
botaoDeLimparTela = tk.Button(telaDeChat, text="Limpar Tela", command=limpaTela)
botaoDeLimparTela.pack(side=tk.LEFT, padx=10, pady=10)

#criando o botão de sair
botaoDeSair = tk.Button(telaDeChat, text="Sair", command=sairDoChat)
botaoDeSair.pack(side=tk.LEFT, padx=10, pady=10)

#vamos inicializar a thread para o cliente ficar recebendo dados
threadRecebeDados = threading.Thread(target=recebeDados, args=[sock, chat])
threadRecebeDados.start()

#iniciando a janela
root.mainloop()
