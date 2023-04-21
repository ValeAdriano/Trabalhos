print('-=-'*10)
print('Emprestimo bancário')
print('-=-'*10)

casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanl o seu salário? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestacao = (casa / anos) / 12
termo = salario / (30 / 100)

if termo < prestacao:
    print('Infelismente sem emprestimo foi negado.')

else:
    print('Seu emprestimo foi aprovado pagando uma prestação de R${} por mês, obrigado. '.format(prestacao))