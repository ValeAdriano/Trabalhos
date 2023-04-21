print('-=-'*8)
print('CUSTO DO DESTINO')
print('-=-'*8)

print('Para qual região você pretende ir? ')
print('[1] Norte')
print('[2] Nordeste')
print('[3] Centro-oeste')
print('[4] Sul')

regiao = int(input())

tipo = int(input('Você pretende ir e voltar? \n[1] sim \n[2] não \n'))

if regiao == 1:
    if tipo == 2:
        print('O valor da sua viagem só de ida é de 500 reais')
    else:
        print('O valor da sua viagem de ida e volta é de 900 reais')

elif regiao == 2:
    if tipo == 2:
        print('O valor da sua viagem só de ida é de 350 reais')
    else:
        print('O valor da sua viagem de ida e volta é de 650 reais')

elif regiao == 3:
    if tipo == 2:
        print('O valor da sua viagem só de ida é de 350 reais')
    else:
        print('O valor da sua viagem de ida e volta é de 600 reais')
        
elif regiao == 4:
    if tipo == 2:
        print('O valor da sua viagem só de ida é de 300 reais')
    else:
        print('O valor da sua viagem de ida e volta é de 550 reais')
        
else:
    print('Região inválida. Por favor, selecione uma opção de 1 a 4.')
