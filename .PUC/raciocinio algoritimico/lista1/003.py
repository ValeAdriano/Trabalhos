print('-=-'*8)
print('PAR OU IMPAR')
print('-=-'*8)

jogador1 = int(input('impar [1]\npar   [2]\n'))

if jogador1 == 1:
    jogador2 = 2
    
    mov1 = int(input('Jogador número 1 joga: '))
    mov2 = int(input('Jogador número 2 joga: '))
    
    resultado = mov1 + mov2
    if resultado % 2 == 0:
        print('O jogador número 2 venceu!!!')
    else:
        print('O jogador número 1 venceu!!!')

elif jogador1 == 2:
    jogador2 = 1
    
    mov1 = int(input('Jogador número 1 joga: '))
    mov2 = int(input('Jogador número 2 joga: '))
    
    resultado = mov1 + mov2
    if resultado % 2 == 0:
        print('O jogador número 1 venceu!!!')
    else:
        print('O jogador número 2 venceu!!!')

