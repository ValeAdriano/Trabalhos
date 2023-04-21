print('-=-'*8)
print('DATA')
print('-=-'*8)


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

print("Data/hora informada: {}/{}/{} {}:{}:{}".format(dia, mes, ano, hora, minuto, segundo))

print("Que informação você deseja acrescentar?")
print('[1] dia')
print('[2] mes')
print('[3] ano')
print('[4] hora')
print('[5] minuto')
print('[6] segundo')


opcao = int(input('Digite a opção desejada: '))
ultimo_dia_mes = 31 if mes in [1, 3, 5, 7, 8, 10, 12] else 30 if mes in [4, 6, 9, 11] else 29 if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 else 28
if opcao == 1:
    qtd_dias = int(input('Digite a quantidade de dias que deseja acrescentar: '))
    while qtd_dias > 0:
        
        if dia < ultimo_dia_mes:
            dia += 1
        else:
            dia = 1
            if mes < 12:
                mes += 1
            else:
                mes = 1
                ano += 1
        qtd_dias -= 1
elif opcao == 2:
    qtd_meses = int(input('Digite a quantidade de meses que deseja acrescentar: '))
    while qtd_meses > 0:
        if mes < 12:
            mes += 1
        else:
            mes = 1
            ano += 1
        qtd_meses -= 1
elif opcao == 3:
    qtd_anos = int(input('Digite a quantidade de anos que deseja acrescentar: '))
    ano += qtd_anos
elif opcao == 4:
    qtd_horas = int(input('Digite a quantidade de horas que deseja acrescentar: '))
    while qtd_horas > 0:
        if hora < 23:
            hora += 1
        else:
            hora = 0
            if dia < ultimo_dia_mes:
                dia += 1
            else:
                dia = 1
                if mes < 12:
                    mes += 1
                else:
                    mes = 1
                    ano += 1
        qtd_horas -= 1
elif opcao == 5:
    qtd_minutos = int(input('Digite a quantidade de minutos que deseja acrescentar: '))
    while qtd_minutos > 0:
        if minuto < 59:
            minuto += 1
        else:
            minuto = 0
            if hora < 23:
                hora += 1
            else:
                hora = 0
                if dia < ultimo_dia_mes:
                    dia += 1
                else:
                    dia = 1
            if mes < 12:
                mes += 1
            else:
                mes = 1
                ano += 1
    qtd_minutos -= 1

elif opcao == 6:
    qtd_segundos = int(input('Digite a quantidade de segundos que deseja acrescentar: '))
    while qtd_segundos > 0:
        if segundo < 59:
            segundo += 1
        else:
            segundo = 0
            if minuto < 59:
                minuto += 1
            else:
                minuto = 0
                if hora < 23:
                    hora += 1
                else:
                    hora = 0
                    if dia < ultimo_dia_mes:
                        dia += 1
                    else:
                        dia = 1
                        if mes < 12:
                            mes += 1
                        else:
                            mes = 1
                            ano += 1
        qtd_segundos -= 1



print("Data/hora informada: {}-{}-{} {}:{}:{}".format(dia, mes, ano, hora, minuto, segundo))
