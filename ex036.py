# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Entre com um número inteiro: '))
opcao = int(input('Em que base deseja mostrá-lo: '
                   '\nDigite (1) para binário '
                   '\nDigite (2) para octal '
                   '\nDigite (3) para hexadecimal '))
if opcao == 1:
    binario = bin(numero).replace('0b','')
    print(f'O número em binário é {binario}')
elif opcao == 2:
    octal = oct(numero).replace('0o','')
    print(f'O número em octal é {octal}.')
else:
    hexadecimal = hex(numero).replace('0x','')
    print(f'O número em hexadecimal é {hexadecimal}')
