print('-=-'*10)
print('GUARDAR NUMEROS NA LISTA')
print('-=-'*10)

lista = []


while True:
    num = lista.append(int((input('Digite um número: '))))
    opc = str(input('Deseja continuar? (y/n)  '))

    if opc == 'n':
        break
    elif opc != 'y':
        print('Opção invalida, tente novamente')
    
    if num in lista:
        print('O número {} é pertence a lista'.format(num))
min = min(lista)
max = max(lista)

print(lista)

print('O maior numero é {} e o menor é {}'.format(max, min))