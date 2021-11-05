# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO, - Média entre 5.0 e 6.9: RECUPERAÇÃO, - Média 7.0 ou superior: APROVADO
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
if (nota2+nota2)/2 >= 7.0:
    print('Aprovado!')
elif (5.0 <= (nota1+nota2)/2 < 7.0):
    print('Recuperação!')
else:
    print('Reprovado!')
