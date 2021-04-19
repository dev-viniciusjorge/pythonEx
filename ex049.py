n = int(input('Digite o numero desejado: '))
for c in range(1, 11):
    tabuada = n * c
    print('{} x {} = {}'.format(n, c, tabuada))