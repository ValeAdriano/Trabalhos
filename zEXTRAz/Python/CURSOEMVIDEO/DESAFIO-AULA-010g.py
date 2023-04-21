distancia = int(input('Qual a distancia da sua viajem?'))
if distancia >= 200:
    preço = (distancia * 0.45)
else:
    preço = (distancia * 0.50)
print('O preço da sua viajem será de R${}.'.format(preço))
