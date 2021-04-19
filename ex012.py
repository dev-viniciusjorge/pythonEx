valor_produto = float(input('Qual o valor do produto? R$ '))
desconto = valor_produto * 0.05
valor_final = valor_produto - desconto
print('O valor do produto, com desconto é R${:.2f}'.format(valor_final))