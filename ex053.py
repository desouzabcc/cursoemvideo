# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date, datetime

maior = 0
menor = 0
atual = date.today().year
for cont in range(0,7):
    ano = int(input('Qual é o ano de nascimento: '))
    if (atual - ano) < 18:
        menor += 1
    else:
        maior += 1
print(f'Foram digitados {menor} menores de idade e {maior} maiores de idade')