#O professor que sortear um dos quatro alunos para apagar o quadro.
#Faça um programa que ajude ele. lendo o nome dos alunos e escrevendo
#o nome do aluno na tela.
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
alunos = [n1,n2,n3,n4]
print(f'O escolhido para apagar o quadro é {random.choice(alunos)}')
