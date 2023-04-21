from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('Parabéns, eu realmente pensei em {}!'.format(computador))
else:
    print('Que pena, na verdade eu pensei em {}'.format(computador))