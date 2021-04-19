from random import randint
print('-='*26)
print('Vou pensar em um numero de 0 a 10, tente adivinhar...')
print('-='*26)
num_usuario = int(input('Em que numero eu pensei? ')) # Jogador tentar acertar
numero = randint(0, 10)  # computador "pensa"
while num_usuario != numero:
    print('Você errou, tente novamente...')
    num_usuario = int(input('Em que numero eu pensei? '))
if num_usuario == numero:
    print('Parabéns, você venceu!')
