número = int(input('Me diga um número qualquer'))
resultado = número % 2

if resultado == 1:
    print('-=-' * 4)
    print('   IMPAR')
    print('-=-' * 4)
else:
    print('-=-' * 3)
    print('   PAR')
    print('-=-' * 3)