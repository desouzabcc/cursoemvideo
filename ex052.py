# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Entre com a frase: ')).strip().upper()
inverso = ' '.join(frase.split())[::-1]
if inverso == frase:
    print(f'O inverso de {frase} é {inverso}, portanto é PALÍNDROMO!')
else:
    print(f'O inverso de {frase} é {inverso}, portanto é PALÍNDROMO!')