n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
n3 = float(input('Digite o número 3: '))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))