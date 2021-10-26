# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
if num1 <= num2 and num1 <= num3:
    print(f'O menor número é {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'O menor número é {num2}')
else:
    print(f'O menor número é {num3}')
if num1 >= num2 and num1 >= num3:
    print(f'O maior número é {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior numero é {num3}')
