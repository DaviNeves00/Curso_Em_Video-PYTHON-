'''
DESAFIO 39
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade 
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar 
- se já passou do tempo do alistamento 
seu programa também deverá mostrar o trempo que falta ou que passou do prazo.
'''

nome = str(input('Olá, qual o seu nome, guerreiro?: ')).title()
nome = nome.split()
idade = int(input('Qual sua idade, {}?: '.format(nome[0])))

falta = 18 - idade
passou = falta - falta * 2

if idade == 18:
    print('Junte seus documentos, você precisa se alistar, guerreiro!')
elif idade < 18:
    print('Seu momento de se alistar ainda não chegou, ainda falta {} anos.'.format(falta))
else:
    print('Seu tempo de alistamento já passou faz {} anos.'.format(passou))