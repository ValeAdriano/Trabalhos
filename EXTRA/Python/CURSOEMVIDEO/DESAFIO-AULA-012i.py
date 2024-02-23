print('{:=^40}'.format('LOJAS VALE'))
v = float(input('Valor do produto: R$'))
print('''Forma de pagamento:
[ 1 ] Dinheiro/Cheque
[ 2 ] À vista no CARTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x ou mais no CARTÃO''')
p = int(input('Como deseja pagar: '))

if p == 1:
    total = v - (v * 10 / 100)
elif p == 2:
    total = v - (v * 5 / 100)
elif p == 3:
    total = v
elif p == 4:
    input('Quantas parcelas: ')
    total = v + (v * 20 / 100)
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(v, total))
