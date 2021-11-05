#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
computador = randint(0,3)
print('Digite 0 para PEDRA\nDigite 1 para PAPEL\nDigite 2 para TESOURA')
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Computador jogou PEDRA')
if computador == 0:
    if jogador == computador:
        print('DEU EMPATE')
    else:
        print('Você Perdeu!!')
elif computador == 1:
    if jogador == computador:
        print('DEU EMPATE')
    elif jogador == 0:
        print('Você Ganhou')
    else:
        print('Você Perdeu!')
elif computador == 1:
    if jogador == computador:
        print('DEU EMPATE')
    elif jogador == 0:
        print('Você Ganhou')
    else:
        print('Você Perdeu!')