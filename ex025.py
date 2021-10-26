# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Entre com a sua frase: ')).upper()
print(f'A letra A aparece {frase.count("A")} vezes na {frase}')
print(f'A primeira ocorrência é na {frase.find("A")+1}ª letra')
print(f'A última ocorrência é na {frase.rfind("A")+1}ª letra')
