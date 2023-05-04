'''resp1 = ''
num = str(input('digite um numero inteiro: '))
tamanho = len(num)
num1 = int(num)
count = 0
while count < tamanho:
    decomp = num // ((tamanho - 1)*10)
    resp0 = str('+ {} x 10 ^{}'.format(decomp, tamanho-1))
    tamanho -+ 1
    resp0 += resp1
print(resp1)'''

resp1 = ''
num = input('digite um numero inteiro: ')
tamanho = len(num)
num1 = int(num)
count = 0
while count < tamanho:
    decomp = num1 // ((tamanho - 1)*10)
    resp0 = str('+ {} x 10 ^{}'.format(decomp, tamanho-1))
    tamanho -= 1
    resp1 += resp0
print(resp1)