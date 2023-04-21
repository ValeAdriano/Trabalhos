soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um {} valor:'.format(c)))
    if n % 2 == 0:
       soma += n
       cont += 1
    else:
        p = 0
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))