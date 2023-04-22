print('-=-'*15)
print('MÉDIAAAAAAAAA')
print('-=-'*15)

num = []
count = 1
soma = 0
for c in range(6):
    numb = int(input('Digite o {}º número: '.format(count)))
    count += 1
    num.append(numb)
    
soma = sum(num)

media = soma / len(num)

print('A média dos números dados é {}'.format(media))