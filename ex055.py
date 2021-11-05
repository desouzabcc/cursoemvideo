# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
homem = ' '
idadeH = ' '
mulheres = 0
idadeM =' '
for cont in range(0,4):
    nome = str(input(f'Entre com o nome da {cont+1}ª pessoa'))
    idade = int(input(f'Entre com a idade da {cont+1}ª pessoa'))
    sexo = str(input(f'Entre com o sexo da {cont+1}ª pessoa (M/F)')).upper()
    soma += idade
    if sexo == M and cont == 0:
        homem = nome
        idadeM = idade
    elif sexo == M and idade > idadeM:
        homem = nome
        idadeM = idade
    elif sexo == F and idade < 20:
        mulheres += 1
print(f'A média de idade das pessoas é {soma/4} '
      f'\nO homem mais velho é o senhor {homem}'
      f'\n e possui {mulheres} menores de 20 anos')
