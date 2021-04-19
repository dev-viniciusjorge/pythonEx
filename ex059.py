from time import sleep
soma = 0
multiplicacao = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('''[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Finalizar programa ''')
choice = int(input('>>> Qual a sua opção? '))

while choice != 5:
    if choice == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
        print('-=' * 25)
    elif choice == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multiplicacao))
        print('-=' * 25)
    elif choice == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
        else:
            print('O maior número é o {}'.format(n2))
        print('-=' * 25)
    elif choice == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite o outro novo número: '))
        print('-=' * 25)
    else:
        choice = int(input('Por favor, digite um valor válido: '))
        print('-=' * 25)
    print('''[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Finalizar programa ''')
    choice = int(input('>>> Qual a sua opção? '))
if choice == 5:
    print('Aguarde...')
    print('-='*25)
    sleep(2)
    print('Programa finalizado com sucesso.')
