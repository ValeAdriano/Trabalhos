print('-=-'*10)
print('NAVEGADOR INTERESTELAR')
print('-=-'*10)

anos_luz = {
 "pc": 0.31,
 "al": 1,
 "ae": 63241.09,
 "ml": 525960.23,
 "sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

# Imprime a lista de unidades de conversão
print("Unidades de tempo disponíveis para conversão:")
for unidade in unidades:
    print("- " + unidade)

# Solicita o valor que se deseja converter
valor = float(input("Valor a ser convertido: "))

# Solicita a unidade origem do valor
unidade_origem = input("Converter de: ")

# Solicita a unidade destino de conversão
unidade_destino = input("Converter para: ")

# Calcula a conversão de unidades
valor_convertido = valor * anos_luz[unidade_origem] / anos_luz[unidade_destino]

# Exibe o valor convertido
print(f"Conversão: {valor} {unidade_origem} = {valor_convertido} {unidade_destino}")
