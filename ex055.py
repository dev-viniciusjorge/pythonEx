maior = 0
menor = 10000
for counter in range(0, 5):
    peso = float(input('Digte seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
