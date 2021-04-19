from datetime import date
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - nascimento
if idade < 18:
    anos_faltantes = 18 - idade
    print('Você ainda não está apto a se alistar, ainda faltam {} anos.'.format(anos_faltantes))
elif idade > 18:
    anos_atrasados = idade - 18
    print('Passou o ano do seu alistamento obrigatório, você está {} anos atrasado.'.format(anos_atrasados))
else:
    print('Está no ano do seu alistamento obrigatório. Você está com {} anos.'.format(idade))
