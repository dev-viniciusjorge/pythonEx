nota1 = float(input('Nota 1 = '))
nota2 = float(input('Nota 2 = '))
media = (nota1 + nota2) / 2
print('Média = {}'.format(media))
if media < 5:
    print('REPROVADO!')
elif media > 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
