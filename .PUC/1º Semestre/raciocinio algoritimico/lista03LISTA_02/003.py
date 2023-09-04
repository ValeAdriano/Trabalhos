print('-=-'*15)
print('NOTAAAAAS')
print('-=-'*15)

notas = []
soma = 0
for c in range(4):
    count = c+1
    num = int(input('Digite o {}o valor: '.format(count)))
    notas.append(num)
    soma += num

media = soma / 4
   
print(media)