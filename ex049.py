# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
par = 0
soma = 0
for cont in range(1,7):
    num = int(input('Entre com um numero inteiro: '))
    if num % 2 == 0:
        soma += num
print(f' a soma dos pares digitados é {soma}')
