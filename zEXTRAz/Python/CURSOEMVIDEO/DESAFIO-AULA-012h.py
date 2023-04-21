print('-=-'*6)
print('CAUCULADOR DE IMC')
print('-=-'*6)
kg = float(input('Qual é seu peso em kg? '))
m = float(input('Qual é a sua altura em m? '))
imc = kg /(m ** 2)

if imc <= 18.5:
    print('Seu IMC pessoal é de {:.2f}. Você está ABAIXO DO PESO'.format(imc))
elif imc <= 25 and imc > 18.5:
    print('Seu IMC pessoal é de {:.2f}. Você está no PESO IDEAL'.format(imc))
elif imc <= 30 and imc > 25:
    print('Seu IMC pessoal é de {:.2f}. Você está SOBREPESO'.format(imc))
elif imc <= 40 and imc > 30:
    print('Seu IMC pessoal é de {:.2f}. Você está com OBESIDADE'.format(imc))
elif imc >= 40:
    print('Seu IMC pessoal é de {:.2f}. Você está com OBESIDADE MÓRBIDA'.format(imc))
