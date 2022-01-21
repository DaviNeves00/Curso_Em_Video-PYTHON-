'''
DESAFIO 36 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
ou então o empréstimo será negado.
'''

nome = str(input('Olá, seja bem vindo(a). com quem estou falando?: ')).title().strip()
nome = nome.split()
casa = float(input('Muito prazer {}! Qual é o valor da imovel que você deseja adquerir? R$'.format(nome[0])))
salario = float(input('Qual é o seu salário mensal?: R$'))
anos = int(input('Em quantos anos pretende pagar o imovel?: '))
anos = anos * 12 

prestacao = casa / anos
valor = salario * 30 / 100

if prestacao <= valor:
    print('Parabéns {}! Seu empréstimo foi aprovado.'.format(nome[0]))
else:
    print('Sinto muito {}. Seu empréstimo não será aprovado.'.format(nome[0]))    
