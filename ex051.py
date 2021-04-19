termo = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10-1) * razao
print(termo, end=' -> ')
for c in range(termo, decimo, razao):
    termo_final = termo + razao
    print(termo_final, end=' -> ')
    termo = termo_final
print('ACABOU')
