# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

sorteio = randint(1, 5)
jogador = int(input('Digite um numero inteiro entre 1 e 5: '))
if sorteio==jogador:
    print('Você acertou!!!!')
else:
    print('Você errou!!!')
