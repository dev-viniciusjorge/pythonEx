import random
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
list = [nome1, nome2, nome3, nome4]
escolhido = random.choice(list)
print('O aluno escolhido foi {}'.format(escolhido))
