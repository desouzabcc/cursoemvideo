# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = int(input('Entre com a primeira medida: '))
r2 = int(input('Entre com a segunda medida: '))
r3 = int(input('Entre com a terceira medida: '))
if r1 < r2 +r3  and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos informados FORMAM um triângulo')
else:
    print('Os segmentos informador NÂO FORMAM um triângulo')
