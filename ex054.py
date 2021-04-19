from datetime import date
maior_idade = 0
menor_idade = 0
for counter in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(counter+1)))
    idade = date.today().year - nascimento
    if idade > 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('''\nAo todo tiveram {} pessoas maiores de idade
E também {} pessoas menores de idade.'''.format(maior_idade, menor_idade))
