from datetime import date

print('-=-'*15)
print('DIFERENCA DE DATA')
print('-=-'*15)


data1_str = input("Digite a primeira data (no formato dd/mm/aaaa): ")
dia, mes, ano = map(int, data1_str.split('/'))
data1 = date(ano, mes, dia)


data2_str = input("Digite a segunda data (no formato dd/mm/aaaa): ")
dia, mes, ano = map(int, data2_str.split('/'))
data2 = date(ano, mes, dia)


diferenca = (data2 - data1).days

print("A diferença entre as datas é de", diferenca, "dias.")