sexo = str(input('Digite seu sexo [M/F]: '))
while sexo != 'M' and sexo != 'F':
    print('Por favor digite M ou F')
    sexo = str(input('Digite seu sexo [M/F]: '))
print('Sexo {} registrado com sucesso.'.format(sexo))
