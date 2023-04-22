print('-=-'*15)
print('INTERCALAÇÃO DE LISTA')
print('-=-'*15)

list1 = []
list2 = []
list3 = []
count = 1

for c in range (5):
    
    num1 = int(input('Digite o {}º digito da lista 1: '.format(count)))
    list1.append(num1)

    num2 = int(input('Digite o {}º digito da lista 2: '.format(count)))
    list2.append(num2)
    
for c in range (len(list1)):
    list3.append(list1[c])
    list3.append(list2[c])
    

print(list3)