n1 = float(input('Digite a primeira nota.'))
n2 = float(input('Digite a segunda nota.'))
m = (n1 + n2)/2
print('A sua média foi {}'.format(m))
if m <= 7.0:
    print('Que pena. Sua nota está abaixo da média, ela foi de {}. Estude mais.'.format(m))
else:
    print('Parabéns! A sua nota está acima de média, ela foi de {}.'.format(m))
