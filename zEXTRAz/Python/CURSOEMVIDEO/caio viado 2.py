print('-=-'*10)
print('Shipping Calculator')
print('-=-'*10)

n1 = int(input('tell me the weight of your packege in kg:'))

if n1 >= 2:
    n2 = (n1 * 1.50)+20

elif n1 > 2 and n1 < 6:
    n2 = (n1 * 3.00)+20

elif n1 > 6 and n1 < 10:
    n2 = (n1 * 4.00)+20

print('-=-'*10)
print('The price of the package: {}'.format(n2))
print('-=-'*10)