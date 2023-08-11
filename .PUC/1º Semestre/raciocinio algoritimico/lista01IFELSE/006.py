print('-=-'*8)
print('EQUAÇÃO DE 2 GRAU')
print('-=-'*8)

a = int(input('Qual o valor de A? '))
b = int(input('Qual o valor de B? '))
c = int(input('Qual o valor de C? '))

delta = b**2 - 4*a*c

resultado1 = (-b + delta**1/2)/ (2 * a)
resultado2 = (-b - delta**1/2)/ (2 * a)
print(resultado1)
print (resultado2)