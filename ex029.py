velocidade = int(input('Digite a velocidade do veículo: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R${}.'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança')
