#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele
variavel = input('Digite alguma coisa: ')
print(f'O tipo primitivo desse valor é {type(variavel)} '
      f'\nSó tem espaços? {variavel.isspace()} '
      f'\nÉ um numero? {variavel.isnumeric()} '
      f'\nÉ alfabético? {variavel.isalpha()} '
      f'\nÉ alfanumérico? {variavel.isalnum()} '
      f'\nEsta em maiúscula? {variavel.isupper()} '
      f'\nEsta em minúscula? {variavel.islower()} '
      f'\nEsta capitalizado? {variavel.istitle()}')
