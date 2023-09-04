print('-=-'*8)
print('PEDRA PAPEL E TESOURA')
print('-=-'*8)

pontos = int(input('Quantos pontos devem ser feitos para ganhar? '))

pont1 = 0
pont2 = 0
    
for c in range(pontos + 1):
    print('[1] pedra\n[2] papel\n[3] tesoura')
    j1 = int(input('Jogador 1:'))
    j2 = int(input('Jogador 2: '))
    
    if j1 == j2:
        print('-=-EMPATE-=-')
        
    elif j1 - j2 == 1:
        print('-=-PONTO JOGADOR 1-=-')
        pont1 += 1        
    elif j1 - j2 == -1:
        print('-=-PONTO JOGADOR 2-=-')
        pont2 += 1     
        
if j1 > j2:
    print('-=-JOGADOR 1 VENCE-=-')

if j1 < j2:
    print('-=-JOGADOR 2 VENCE-=-')