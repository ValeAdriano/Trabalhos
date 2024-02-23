a = int(input('Primeiro valor:'))
b = int(input('Primeiro valor:'))
c = int(input('Primeiro valor:'))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    manor = c
#Verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('-=-O menor valor digitado foi {}-=-'.format(menor))
print('-=-O maior valor digitado foi {}-=-'.format(maior))