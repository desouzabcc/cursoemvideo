# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('Qual é o ano de nascimento: '))
idade = atual - ano
if (idade < 18):
    print(f'Faltam {18 - idade} ano(s) para o alistamento. O mesmo será em {atual + (18 - idade)}')
elif (idade == 18):
    print('Você deve se alistar imediatamente!')
else:
    print(f'O seu alistamento deveria ter sido a {idade - 18} ano(s) atrás, no ano de {atual - (idade - 18)}')