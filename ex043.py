peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros (ex: 1.70): '))
imc = peso / pow(altura, 2)
print('O valor do seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
