a = float(input('Digite o lado a do triangulo: '))
b = float(input('Digite o lado b do triangulo: '))
c = float(input('Digite o lado c do triangulo: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triangulo')
    if a == b and a == c:
        print('Formará um triângulo equiátero.')
    elif a != b and a != c:
        print('Formará um triângulo escaleno.')
    else:
        print('Formará um triangulo isóceles.')
else:
    print('As retas não podem formar um triangulo')
