#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele
variavel = input('Digite alguma coisa: ')
print(f'O tipo primitivo desse valor é {type(variavel)} \nSó tem espaços? {variavel.isspace()} \nÉ um numero? {variavel.isnumeric()} \nÉ alfabético? {variavel.isalpha()} \nÉ alfanumérico? {variavel.isalnum()} \nEsta em maiúscula? {variavel.isupper()} \nEsta em minúscula? {variavel.islower()} \nEsta capitalizado? {variavel.istitle()}')
