salario_inicial = float(input('Digite o salário inicial do funcionário: R$ '))
ajuste = salario_inicial * 0.15
salario_ajustado = salario_inicial + ajuste
print('Um funcionário que ganhava R${:.2f} por mês, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario_inicial, salario_ajustado))