print('caucula necessidade de tinta')
l = float(input('Qual é a largura da sua parede'))
a = float(input('Qual a altura da sua parede'))
área = l * a
print('{}metros quadrados'.format(área))
t = (área / 2)
print('Você precisará de {} litros de tinta'.format(t))
