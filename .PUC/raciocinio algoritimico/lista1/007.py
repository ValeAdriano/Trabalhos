print('-=-'*8)
print('ANIVERSÁRIO')
print('-=-'*8)


data = int(input('Qual o dia do seu aniversário?: '))
mes = int(input('Qual o mês do seu aniversário?: '))
ano = int(input('Qual o ano do seu aniversário (ex: 2005)?: '))

print('Data simples (ex: 16/03/05)             [1]')
print('Data abreviada (ex: 16/mar/05)          [2]')
print('Data completa (ex: 16 de março de 2005) [3]')
tipo = input('')

if mes == 1:
    abreviada1 = 'jan'
    completa1 = 'janeiro'
if mes == 2:
    abreviada1 = 'fev'
    completa1 = 'fevereiro'
if mes == 3:
    abreviada1 = 'mar'
    completa1 = 'marco'
if mes == 4:
    abreviada1 = 'abr'
    completa1 = 'abril'
if mes == 5:
    abreviada1 = 'mai'
    completa1 = 'maio'
if mes == 6:
    abreviada1 = 'jun'
    completa1 = 'junho'
if mes == 7:
    abreviada1 = 'jul'
    completa1 = 'julho'
if mes == 8:
    abreviada1 = 'ago,'
    completa1 = 'agosto'
if mes == 9:
    abreviada1 = 'set'
    completa1 = 'setembro'
if mes == 10:
    abreviada1 = 'out'
    completa1 = 'outubro'
if mes == 11:
    abreviada1 = 'nov'
    completa1 = 'novembro'
if mes == 12:
    abreviada1 = 'dez'
    completa1 = 'dezembro'
    
if tipo == 1:
    print('A sua data de aniversário de forma simples é: {}/{}/{}'.format(data, mes, ano))

if tipo == 2:
    print('A sua data de aniversário de forma abreviada é: {}/{}/{}'.format(data, abreviada1, ano))
    
if tipo == 3:
    print('A sua data de aniversário de forma completa é: {} de {} de {}'.format(data, completa1, ano))