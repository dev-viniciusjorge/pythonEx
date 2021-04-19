idade_maior = 0
nome_maior = ''
soma_idade = 0
count_mulheres = 0
media = 0
for counter in range(1, 5):
    print('--------- {}° PESSOA ---------'.format(counter))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idade += idade
    media = soma_idade / counter
    if idade > idade_maior and sexo == 'M':
        nome_maior = nome
        idade_maior = idade
    if idade < 20 and sexo == 'F':
        count_mulheres += 1
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_maior, idade_maior))
print('No grupo tem {} mulheres com menos de 20 anos.'.format(count_mulheres))
