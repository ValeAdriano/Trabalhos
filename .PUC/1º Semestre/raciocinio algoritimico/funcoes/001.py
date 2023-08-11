print('-=-'*15)
print('FATORAL')
print('-=-'*15)

def fatorial(num):
    fatorial = 1 
    for c in range(num-1):
        fatorial *= c +1
    return fatorial

n = int(input('Digite um número para calcular o seu fatorial: '))
print('O fatorial de {} é {}'.format(n, fatorial(n)))