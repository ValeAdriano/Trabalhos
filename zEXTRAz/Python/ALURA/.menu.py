print("*********************************")
print("Hub de jogos:")
print("*********************************")

print('qual jogo deseja jogar?')
print('[1] Adivinhação [2] Forca')
jogo = int(input('Quero jogar o jogo: '))

if jogo == 1:
    import adivinhacao
elif jogo == 2:
    import forca
else:
    print('Opção invalida tente novamente :(')
