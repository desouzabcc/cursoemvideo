# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais, - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
r1 = int(input('Entre com a primeira medida: '))
r2 = int(input('Entre com a segunda medida: '))
r3 = int(input('Entre com a terceira medida: '))
if r1 < r2 +r3  and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Eles formam um TRIÂNGULO ISÓSCELES ')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Eles formam um TRIÂNGULO EQUILÁTERO')
    elif (r1 != r2) and (r1 != r2) and (r2 != r3):
        print('Eles formam um TRIÂNGULO ESCALENO')
else:
    print('Os segmentos informados NÃO FORMAM UM TRIÂNGULO')