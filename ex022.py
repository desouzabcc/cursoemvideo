# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número inteiro: '))
n1 = numero // 1000
numero = numero % 1000
n2 = numero // 100
numero = numero % 100
n3 = numero // 10
numero = numero % 10
n4 = numero // 1
print(f'O número digitado tem: \nMilhar = {n1}'
      f'\nCentena = {n2}'
      f'\nDezena = {n3}'
      f'\nUnidade = {n4}')


