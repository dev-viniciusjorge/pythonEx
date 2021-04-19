from random import randint
print('-='*26)
print('Vou pensar em um numero de 0 a 5, tente adivinhar...')
print('-='*26)
num_usuario = int(input('Em que numero eu pensei? ')) # Jogador tentar acertar
numero = randint(0, 5)  # computador "pensa"
print('Pensei no número {}.'.format(numero))
if num_usuario == numero:
    print('Parabéns, você venceu!')
else:
    print('Você perdeu!')
