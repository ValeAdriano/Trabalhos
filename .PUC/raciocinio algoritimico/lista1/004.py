print('-=-'*8)
print('CALCULADORA DE DESCONTO')
print('-=-'*8)

etiqueta = float(input('Qual o valor de etiqueta do protuto'))

print('Como deseja pagar o produto?')
print('[1] a vista dinheito ou cheque 10%')
print('[2] a vista cartão de crédito 15%')
print('[3] duas vezes sem juros')
print('[4] tres vezes juros de 10%')
opcao = int(input(''))

if opcao == 1:
    desconto = etiqueta * 0.10
    valorfinal = etiqueta - desconto 
if opcao == 2:
    desconto = etiqueta * 0.15
    valorfinal = etiqueta - desconto 
if opcao == 3:
    valorfinal = etiqueta
if opcao == 4:
    juros = etiqueta * 0.10
    valorfinal = etiqueta + juros
    
print('O valor final a ser pago será de {}'.format(valorfinal))