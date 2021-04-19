from datetime import date
nascimento = int(input('Digite a sua data de nascimento: '))
idade = date.today().year - nascimento
print('Sua idade: {} anos.'.format(idade))
if idade < 0:
    print('Idade não existente.')
elif idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
