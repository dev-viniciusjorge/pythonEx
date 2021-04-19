distancia = float(input('Digite a distancia percorrida me Km: '))
if distancia <= 200:
    valor = 0.5 * distancia
else:
    valor = 0.45 * distancia
print('O valor da viagem será de R${:.2f}'.format(valor))
