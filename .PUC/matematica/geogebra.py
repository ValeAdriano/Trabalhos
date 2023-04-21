'''print('-=-'*8)
print('PLANO DE TELEFONE')
print('-=-'*8)

print('Qual plano você pretende usar?')
print('[1] 14 reais mais 3 centavos por minuto')
print('[2] 29 reais ilimitado')

plano = int(input(''))

if plano == 1:

    min = int(input('Quantos minutos voce passa por mes: '))

    custo = 14 + min * 0.03

elif plano == 2:

    custo = 29

print('Você deve pagar um total de {} pelo seu plano'.format(custo))'''



x = int(input('Quantos minutos? '))
print('O valor a ser pago sera R${:.2f}'.format(x*0.03+14))









