import random

i = 0
numbs = []
mult3 = []
impar = []
par = []


for i in range(100):
    
    num = random.randint(1, 100)

    
    numbs.append(num)
    i += 1

print(numbs)

for c in numbs:

    if c % 3 == 0:
        print("{} é mutiplo de 3".format(c))
        mult3.append(c)

    elif c % 2  == 0:
        print("{} é par".format(c))
        par.append(c)
    
    else:
        print("{} é impar".format(c))
        impar.append(c)

print("---RESULTADO---")
print(mult3)
print('São multiplos de 3')
print("---------------")
print(par)
print('São pares')
print("---------------")
print(impar)
print('São impares')
print("---------------")



    


