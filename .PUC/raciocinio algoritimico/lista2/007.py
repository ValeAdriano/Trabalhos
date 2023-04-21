print('-=-'*8)
print('CONTADOR DE AAAAA')
print('-=-'*8)

palavralist = []

contador_a = 0

while True:
    palavra = input("Digite uma palavra (ou pressione 'enter' para sair): ")
    if palavra == "":
        break
    palavralist.append(palavra)

contador_a = 0
for palavra in palavralist:
    for letra in palavra:
        if letra == "a" or letra == "A":
            contador_a += 1

print(f"O número de letras A na lista de palavras é: {contador_a}")