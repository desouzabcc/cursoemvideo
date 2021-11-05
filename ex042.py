# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o seu peso(kg): '))
altura = float(input('Qual á a sua altura(mt): '))
imc = peso /(altura * altura)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você esta Abaixo do Peso!')
elif imc < 25:
    print('Você esta no Peso Ideal')
elif imc < 30:
    print('Você esta com Sobrepeso!')
elif imc < 40:
    print('Você esta com Obesidade!')
elif imc > 40:
    print('Você esta com Obesidade Mórbida!')
