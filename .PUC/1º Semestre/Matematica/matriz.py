linha = int(input("Digite o número de linhas da matriz: "))
coluna = int(input("Digite o número de colunas da matriz: "))

# Inicialize uma matriz vazia
matrix = []

# Preencha a matriz com os valores de entrada do usuário
for i in range(linha):
    row = input(f"Digite os {coluna} valores da linha {i+1} separados por espaço ou vírgula: ")
    matrix.append([float(x) for x in row.split()])

# Imprima a matriz
print(matrix)
