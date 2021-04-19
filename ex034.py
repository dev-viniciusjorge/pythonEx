salario = float(input('Digite seu salário: '))
if salario > 1250:
    salario = salario + (salario*0.1)
else:
    salario = salario + (salario*0.15)
print('Seu novo salário será de R${:.2f}'.format(salario))