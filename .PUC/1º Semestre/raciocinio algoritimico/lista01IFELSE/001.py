print('-=-'*8)
print('CALCULADORA DE PESO IDEAL')
print('-=-'*8)

altura = float(input('Qual a sua altura ?'))
sexo = int(input('Sexo: \n MASCULINO [1] \n FEMININO  [2] '))

if sexo == 1:
    pideal = (72.7 * altura) - 58
elif sexo == 2:
    pideal = (62.1 * altura) - 44.7

print('Seu peso ideal é ', pideal)