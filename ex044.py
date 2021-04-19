valor = float(input('Digite o valor do produto: R$ '))
print('''Escolga a forma de pagamento
[1] - À vista no dinheiro/cheque com 20% de desconto
[2] - À vista no cartão com 5% de desconto
[3] - Em até 6x no cartão sem juros
[4] - Em 7x ou mais no cartão com juros''')
opcao = int(input('Sua opção: '))
while 1 > opcao > 4:
    opcao = int(input('Favor, digite um número entre 1 e 4: '))
if opcao == 1:
    desconto_avista = valor - (valor * 0.2)
    print('Valor com 20% de desconto: R${:.2f}'.format(desconto_avista))
elif opcao == 2:
    desconto_cartao = valor - (valor * 0.05)
    print('Valor com 5% de desconto: R${:.2f}'.format(desconto_cartao))
elif opcao == 3:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    while 1 > parcela > 6:
        parcela = int(input('Favor, digite uma parcela entre 2 e 6 vezes: '))
    valor_parcela = valor / parcela
    print('Você parcelou o valor de R${:.2f} em {}x. O valor da parcela será de R$ {:.2f} '.format(valor, parcela, valor_parcela))
else:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    while parcela < 7:
        parcela = int(input('Favor, digite uma parcela a partir de 7 vezes: '))
    valor_parcela = valor / parcela
    valor_parcela = valor_parcela + (valor_parcela * 0.2)
    print('Você parcelou o valor de R${:.2f} em {}x. O valor da parcela será de R$ {:.2f} '.format(valor, parcela, valor_parcela))