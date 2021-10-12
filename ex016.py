#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
import math
oposto = float(input('Qual é o cateto oposto: '))
adjacente = float(input('Qual é o cateto adjacente: '))
print(f'O tamanho da hipotenusa é {math.hypot(oposto,adjacente):.2}')
