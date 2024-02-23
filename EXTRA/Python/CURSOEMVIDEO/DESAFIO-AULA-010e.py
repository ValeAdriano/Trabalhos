velocidade = float(input('Qual é a velocidade do carro?'))
if velocidade > 80:
    print('-=-' * 20)
    print('  MULTADO! Você exedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('        Você deverá pagar uma multa de R${:.2f}!'.format(multa))
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('          Tenha um bom dia! Digija com segurança!')
    print('-=-' * 20)