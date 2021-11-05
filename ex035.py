# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
if (valor/(anos*12))<=(salario*30/100):
    print(f'empréstimo aprovado! serão {anos*12} parcelas de R${valor/(anos*12):.2f}')
else:
    print(f'empréstimo negado! sua parcela excede 30% de sua renda!')
