print('-=-'*10)
print('GUARDAR NUMEROS NA LISTA')
print('-=-'*10)

c = 0
lista = []


for c in range (5):
    lista.append(int((input('Digite um número: '))))


min = min(lista)
max = max(lista)

print(lista)

print('O maior numero é {} e o menor é {}'.format(max, min))