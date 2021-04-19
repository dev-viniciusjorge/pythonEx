dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodado? '))
valor_dia = dias * 60
valor_km = km * 0.15
valor_final = valor_dia + valor_km
print('O valor a pagar é de R${:.2f}'.format(valor_final))
