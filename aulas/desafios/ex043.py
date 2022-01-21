'''
DESAFIO 43
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status, de acordo com a tabela:
- abaixo de 18,5: abaixo do peso
- entre 18,5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obsidade
- acima de 40: obsidade mórbida
'''
nome = str(input('Olá, qual o seu nome?: ')).title().strip()
nome = nome.split()
peso = float(input('Seja bem vindo(a) {}. Poderia nos informar seu peso?: '.format(nome[0])))
altura = float(input('você poderia nos informar sua altura (em metros): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('{}, você está \033[36mabaixo\033[m do peso.'.format(nome[0]))
elif imc == 18.5 or imc < 25:
    print('{}, você está no peso \033[32mideal\033[m.'.format(nome[0]))
elif imc == 25 or imc < 30:
    print('{}, você está com \033[33msobrepeso\033[m.'.format(nome[0]))
elif imc == 30 or imc < 40:
    print('{}, você está com \033[37mobsidade\033[m.'.format(nome[0]))
else:
    print('{}, você está com \033[31mobsidade morbida\033[m.'.format(nome[0]))