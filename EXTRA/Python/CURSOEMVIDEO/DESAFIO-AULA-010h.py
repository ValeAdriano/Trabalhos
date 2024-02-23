ano = int(input('Escreva um ano:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('-=-O ano {} E BISSEXTO-=-'.format(ano))
else:
    print('-=-O ano {} NÃO é BISSEXTO-=-'.format(ano))
