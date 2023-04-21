print('-=-'*4)
print('ALISTAMENTO')
print('-=-'*4)
ano = int(input('Em que ano você nasceu?'))
idade = 2020 - ano
dif = idade - 18
faltam = 18 - idade
print('Você tem {}.'.format(idade))

if idade == 18:
    print('Esse é o ano que você deve se alistar.')
elif idade > 18:
    print('Você deveria ter se alistado há {}.'.format(dif))
elif idade < 18:
    print('Você irá de alistar em {}.'.format(faltam))