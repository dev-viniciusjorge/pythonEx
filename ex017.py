from math import hypot
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
