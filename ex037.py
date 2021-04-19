numero = int(input('Digite o número inteiro que deseja converter: '))
print('Para qual base deseja converter? ')
print('''Escolha uma das bases para a conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
choice = int(input('Sua escolha: '))
while choice < 1 or choice > 3:
    choice = int(input('Por favor, digite um número inteiro entre 1 e 3: '))
if choice == 1:
    print('O número {} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif choice == 2:
    print('O número {} convertido para octal é {}'.format(numero, oct(numero)[2:]))
else:
    print('O número {} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
