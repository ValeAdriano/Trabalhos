print('-=-'*8)
print('VALIDADOR DE CPF')
print('-=-'*8)

cpf = []

for i in range(11):
    while True:
        digito = input(f"Digite o {i+1}º dígito do CPF: ")
        if digito.isdigit():
            cpf.append(int(digito))
            break
        else:
            print("Por favor, digite apenas números.")

soma = 0
for i in range(9):
    soma += cpf[i] * (10 - i)

resto = soma % 11
digito1 = 0 if resto < 2 else 11 - resto

if cpf[9] != digito1:
    print("CPF inválido.")
    exit()

soma = 0
for i in range(10):
    soma += cpf[i] * (11 - i)

resto = soma % 11
digito2 = 0 if resto < 2 else 11 - resto

if cpf[10] != digito2:
    print("CPF inválido.")
    exit()

print("CPF válido!")