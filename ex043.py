# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Qual é o valor do produto: '))
print('Digite 1 para pagamento a vista em dinheiro '
      '\nDigite 2 para pagamento à vista no cartão '
      '\nDigite 3 para pagamento em 2x no cartão \nDigite 4 para pagamento em 3x ou mais no cartão')
condicao = int(input('Qual é a forma de pagamento?'))
if condicao == 1:
    print(f'O valor final do produto é R$ {preco - (preco * 10 / 100):.2f}')
elif condicao == 2:
    print(f'O valor final do produto é de R$ {preco - (preco * 5 / 100):.2f}')
elif condicao == 3:
    print(f' O valor do parcelamento é de 2x de R$ {(preco / 2):.2f}')
elif condicao == 4:
    limite= int(input('Quantas parcelas deseja fazer: '))
    print(f'O valor das parcelas será de R$ {(preco + (preco * 20 / 100)) / limite:.2f}')
