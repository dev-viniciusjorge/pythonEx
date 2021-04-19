valor =float(input('Qual o valor que você tem em seu banco? R$'))
dolar = valor / 5.75
print('Com o valor de R${:.2f}, você consegue comprar US${:.2f}'.format(valor, dolar))