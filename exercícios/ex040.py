'''
DESAFIO 40
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado 
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado
'''

nota1 = float(input('Qual a sua primeira nota?: '))
nota2 = float(input('Qual é a sua segunda nota?: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi \033[31m{}\033[m, você foi reprovado!'.format(media))
elif media == 5.0 or media < 6.9:
    print('Sua média foi \033[33m{}\033[m, você está de recuperação!'.format(media))
else:
    print('Sua média foi \033[32m{}\033[m, você foi aprovado!'.format(media))
    
