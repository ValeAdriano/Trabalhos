print('-=-'*8)
print('NOME COMPLETO')
print('-=-'*8)

nome = []

while True:
    nomecompleto = input('Qual o seu nome completo? (quando terminar digite 0) ')
    if nomecompleto == '0':
        break
    nome.append(nomecompleto)
    tamanho = len(nome)

print('Olá {}{}'.format(nome[0], nome[tamanho - 1] ))