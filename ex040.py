#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM, - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR, - Até 25 anos: SÊNIOR e - Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
ano = int(input(' Qual é o ano de nascimento do atleta: '))
if (atual - ano) <= 9:
    print('Este atleta é MIRIM')
elif (atual - ano) <= 14:
    print('Este atleta é INFANTIL')
elif (atual - ano) <= 19:
    print('Este atleta é JÚNIOR')
elif (atual - ano) <=25:
    print('Este atleta é SÊNIOR')
elif (atual - ano) > 25:
    print('Este atleta é MASTER')
