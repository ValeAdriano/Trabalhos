print('-=-'*15)
print('MAIOR E MENOR')
print('-=-'*15)

numb = []

count = 0
while count < 5:
    numb.append(int(input('Digite um valor inteiro: ')))
    count += 1



numb.sort()

if 5 in numb:

    print('O número 5 pertence a lista')

print(numb)

