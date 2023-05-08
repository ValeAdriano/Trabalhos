print('-=-'*15)
print('LISTA')
print('-=-'*15)

vetor = []

for c in range(10):
    count = c+1
    num = int(input('Digite o {}o valor: '.format(count)))
    vetor.append(num)

vetor.sort(reverse=True)
   
print(vetor)