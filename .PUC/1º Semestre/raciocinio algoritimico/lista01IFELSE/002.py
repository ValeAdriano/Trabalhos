print('-=-'*8)
print('CALCULADORA DE IMC')
print('-=-'*8)

peso = float(input('qual o seu peso? '))
altura = float(input('qual a sua altura?'))

imc =  (altura ** 2)  / peso 


if imc < 18.5:
    print('Voce está a baixo do normal')
elif imc > 18.5 and imc < 25:
    print('voce está no peso normal')
elif imc > 25 and imc < 30:
    print('Voce está a cima do peso')
elif imc > 30:
    print('Você está obeso')