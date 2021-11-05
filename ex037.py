# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior, O segundo valor é maior ou - Não existe valor maior, os dois são iguais
primeiro = int(input('Qual é o primeiro numero: '))
segundo = int(input('Qual é o segundo numero: '))
if primeiro > segundo:
    print('O primeiro numero é maior que o segundo! ')
elif segundo > primeiro:
    print('O segundo numero é maior que o primeiro!')
else:
    print('Não existe numero maior, os dois são iguais!')