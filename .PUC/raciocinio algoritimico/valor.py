nome = str(input('qual o nome do produto'))
valor = float(input('qual o valor do produdo? '))
quant = int(input('qual a quantidade do produto? '))

total = valor * quant
desc = total * 0.15
totaldesc = total - desc

print('O valor de {} {} sem o desconto é {} e com o desconto de 15% é {}'.format(quant, nome, total, totaldesc))