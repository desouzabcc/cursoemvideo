# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0
for cont in range(0,5):
    peso = float(input('Digite o peso: '))
    if cont == 1:
        menor = peso
        maior = peso
    elif peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
print(f'O maior peso digitado foi {maior} e o menor foi {menor}')
