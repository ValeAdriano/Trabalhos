print('-=-'*10)
print('Triangle type finder')
print('-=-'*10)

n1 = int(input('first side of the triangle:'))
n2 = int(input('second side of the triangle:'))
n3 = int(input('third side of the triangle:'))



if n1 == n2 or n1 == n3 or n2 == n3:
    iso = int('n1 + n2 + n3')
    print('This is a isosceles Triangle. The perimeter of the triangle is {}'.format(iso))
elif n1 == n2 == n3:
    equi = int('n1 + n2 +n3')
    print('This is a equilateral Triangle. The perimeter of the triangle is {}'.format(equi))
elif n1 != n2 != n3:
    sca = int('n1 + n2 + n3')
    print('This is a scalene Triangle. The perimeter of the triangle is {}'.format(sca))
else:
    print('erro insert new numbers'*100)