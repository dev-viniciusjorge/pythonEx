largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A parede tem a dimensão de {} x {} e sua area é de {} metros quadrados.'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
