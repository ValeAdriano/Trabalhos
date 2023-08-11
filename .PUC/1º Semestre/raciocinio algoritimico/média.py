quant = 1
total = 0
while quant <= 4:
    nota = int(input('Qual foi a sua nota na prova {}'.format(quant)))
    quant = quant + 1
    total = total + nota
media = total/4
print(media)