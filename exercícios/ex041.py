'''
DESAFIO 41
A confederação nacional de natação precisa de um programa 
que leia o ano de nascimento de atletas e mostre sua categoria,
de acordo com a idade:
até 9 anos: mirim
até 14 anos: infantil
até 19 anos: júnior
até 20 anos: sênior
acima de 20 anos: master
'''

nome = str(input('Olá, qual o seu nome?: ')).title()
nome = nome.split()
ano = int(input('Seja bem vindo(a) {}. Poderia nos informar o seu ano de nascimento?: '.format(nome[0])))
data = 2022 - ano

if data <= 9:
    print('Muito bem {}, a sua categoria é \033[32mMIRIM\033[m.'.format(nome[0]))
elif data <= 14:
    print('Muito bem {}, a sua categoria é \033[33mINFANTIL\033[m.'.format(nome[0]))
elif data <= 19:
    print('Muito bem {}, a sua categoria é \033[36mJÚNIOR\033[m.'.format(nome[0]))
elif data == 20:
    print('Muito bem {}, a sua categoria é \033[36mSÊNIOR\033[m.'.format(nome[0]))
else:
    print('Muito bem {}, a sua categoria é \033[31mMASTER\033[m.'.format(nome[0]))