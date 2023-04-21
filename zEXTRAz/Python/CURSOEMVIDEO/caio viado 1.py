print('-=-'*10)
print('Electricity Bill calculator ')
print('-=-'*10)
n1 = int(input('number of units consumed:'))


if n1 < 200:
    n2 = (n1 * 1.20)

elif n1 > 199 and n1 < 400:
    n2 = (n1 * 1.50)

elif n1 > 399 and n1 < 600:
    n2 = (n1 * 1.80)

elif n1 > 599:
    n2 = (n1 * 2)

print('Eletricity bill will be {}'.format(n2))