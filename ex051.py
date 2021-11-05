# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número: '))
divisor = 1
for cont in range(2,numero + 1):
    if numero % cont == 0:
        divisor += 1;
if (divisor == 2 or divisor == 1):
    print(f'O numero {numero} é PRIMO')
else:
    print(f'O numero {numero} NÃO É PRIMO')