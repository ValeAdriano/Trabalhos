print('-=-'*8)
print('NATALIDADE')
print('-=-'*8)

paisA = 5000000
paisB = 7000000
ano = 0 
while paisA < paisB:
    paisA += (paisA * 0.03)
    paisB += (paisB * 0.02)
    ano += 1 

print('O país A levou {} anos para ultrapassar o país B'.format(ano))