print('-=-'*15)
print('DECIMAL PARA HEXADECIMAL')
print('-=-'*15)




decimal = input('Digite um número DECIMAL')
hexadecimal = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(remainder + 55) + hexadecimal
    decimal = decimal // 16

print(hexadecimal)