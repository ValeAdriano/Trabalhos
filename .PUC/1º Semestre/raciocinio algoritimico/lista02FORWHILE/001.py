print('-=-'*8)
print('TEMPO DE MEIA VIDA')
print('-=-'*8)
step = 0
massa = float(input('Qual a massa do material:'))
while massa > 0.5:
    massa = massa/2
    step += 1
tempo = step * 50

print('O material em {} segundos decaiu a massa de {}'.format(tempo, massa))

