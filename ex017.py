#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Qual é o ângulo? '))
print(f'O valor do seno é {math.sin(math.radians(angulo)):.2f},\no cosseno é {math.cos(math.radians(angulo)):.2f} e a\ntangente é {math.tan(math.radians(angulo)):.2f}')
