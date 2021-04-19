print('-='*27)
valor_casa = float(input('Digite o valor da casa que deseja comprar: R$ '))
salario = float(input('Digite o salário que você recebe: R$ '))
anos = int(input('Digite em quantos anos deseja parcelar: R$ '))
print('-='*27)
prestacao = (valor_casa / anos) / 12
minimo = salario * 0.3
if prestacao <= minimo:
    print('Empréstimo aprovado!')
    print('Prestação: R$ {:.2f}'.format(prestacao))
else :
    print('Empréstimo negado!')

