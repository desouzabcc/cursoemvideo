# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o valor do salário: '))
if salario <= 1250.00:
    print(f'O salário de {salario} Reais com 15% de aumento é {salario + (salario * 15 / 100)}')
else:
    print(f'O salário de {salario } Reais com 10% de aumento é {salario + (salario * 10 / 100)}')