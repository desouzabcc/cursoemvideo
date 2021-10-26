# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual é a velocidade atual do carro: '))
if velocidade <= 80.0 :
    print('Você esta dentro da velocidade permitida!!')
else:
    print(f'Você esta acima da velocidade permitida. Sua multa é de {(velocidade-80.0)*7} Reais')
