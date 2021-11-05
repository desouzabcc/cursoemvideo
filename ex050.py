# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Qual é o primeiro termo da PA: '))
razao = int(input('Qual é a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for cont in range(primeiro,decimo + razao, razao):
    print(cont)
print('fim')