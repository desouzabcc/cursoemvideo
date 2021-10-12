#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta
#uma área de 2 metros quadrados
largura = int(input('Qual é a largura da parede: '))
altura = int(input('Qual é a altura da parede: '))
print(f'A parede tem {largura*altura} metros quadrados e precisa de {(largura*altura)/2} lata(s) de tinta')
