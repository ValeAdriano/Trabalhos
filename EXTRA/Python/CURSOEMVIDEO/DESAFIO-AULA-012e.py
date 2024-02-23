print('-=-'*5)
print('MÉDIA ESCOLAR')
print('-=-'*5)
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
média =  (n1 + n2)/2
if média >= 7.0:
    print('''Tirando {} e {} a sua média será de {}.
O aluno está APROVADO.'''.format(n1, n2, média))
elif média < 7.0 and média >= 6.0:
    print('''Tirando {} e {} a sua média será de {}.
O aluno está de RECUPERAÇÃO. '''.format(n1, n2, média))
elif média < 6.0:
    print('''Tirando {} e {} a sua média será de {}.
O aluno está REPROVADO'''.format(n1, n2, média))
