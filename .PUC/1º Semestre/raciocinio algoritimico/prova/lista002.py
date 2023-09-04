print('-=-'*15)
print('NUMEROS UNICOS')
print('-=-'*15)

numb = []
count = 0


while count < 5:
     num = int(input('Digite um número inteiro: '))
    

     if num in numb:
         print('-=-Este número já pertence a lista-=-')

     else:
          numb.append(num)
            
          count += 1

print(numb)