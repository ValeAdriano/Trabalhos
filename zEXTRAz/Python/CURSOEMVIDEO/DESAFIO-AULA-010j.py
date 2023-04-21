salário = float(input('Qual é o seu salário atual?'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
if salário > 1250:
    novo = salário + (salário * 10/100)
print('-=-O seu novo salário será de {}'.format(novo))
