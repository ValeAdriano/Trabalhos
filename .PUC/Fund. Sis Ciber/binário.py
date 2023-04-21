print('-=-'*15)
print('CALCULADRA BINÁRIO, HEXADECIMAL E OCTAL')
print('-=-'*15)

print('Decimal para base X [1]')
print('Base X para decimal [2]')
opcao_regra = int(input(''))
    
if opcao_regra == 2:
    print('Binário para decimal [1]')
    print('Hexadecimal para decimal [2]')
    print('Octal para decimal [3]')
    opcao = int(input(''))

    if opcao == 1:
        numero_binario = input('Digite um número em BINÁRIO: ')
        numero_decimal = int(numero_binario, 2)
        print(numero_decimal)
    elif opcao == 2:
        numero_binario = input('Digite um número em HEXADECIMAL: ')
        numero_decimal = int(numero_binario, 16)
        print(numero_decimal)
    elif opcao == 3:
        numero_binario = input('Digite um número em OCTAL: ')
        numero_decimal = int(numero_binario, 8)
        print(numero_decimal)
elif opcao_regra == 1:
    print('Decimal para binário [1]')
    print('Decimal para hexadecimal [2]')
    print('Decimal para octal [3]')
    opcao = int(input(''))
    if opcao == 1:
        numero_decimal = int(input('Digite um número DECIMAL: '))
        numero_binario = bin(numero_decimal)[2:]
        print(numero_binario)
    elif opcao == 2:
        numero_decimal = int(input('Digite um número DECIMAL: '))
        numero_hexa = hex(numero_decimal)[2: ]
        print(numero_hexa)
    elif opcao == 3:
        numero_decimal = int(input('Digite um número DECIMAL: '))
        numero_octal = oct(numero_decimal)[2: ]
        print(numero_octal)

