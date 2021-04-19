import random
escolha = input('Pedra, papel ou tesoura? ')
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
list = [pedra, papel, tesoura]
escolha_pc = random.choice(list)
print('Você escolheu {}.'.format(escolha))
print('O computador escolheu {}. '.format(escolha_pc))
if escolha_pc == pedra and escolha == tesoura:
    print('Que pena, você PERDEU!')
elif escolha_pc == papel and escolha == pedra:
    print('Que pena, você PERDEU!')
elif escolha_pc == tesoura and escolha == papel:
    print('Que pena, você PERDEU!')
elif escolha == pedra and escolha_pc == tesoura:
    print('Parabéns, você VENCEU!')
elif escolha == papel and escolha_pc == pedra:
    print('Parabéns, você VENCEU!')
elif escolha == tesoura and escolha_pc == papel:
    print('Parabéns, você VENCEU!')
else:
    print('Ambos jogaram o mesmo, deu EMPATE!')

