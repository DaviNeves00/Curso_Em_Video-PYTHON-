'''
DESAFIO 38
escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior 
- o segundo valor é maior 
- não existe valor maior ambos são iguais
'''

n1 = str(input('Escolha algum número inteiro: '))
n2 = str(input('Agora escolha outro número inteiro: '))

if n1 > n2:
    print('O número \033[32m{}\033[m é maior.'.format(n1))
elif n1 < n2:
    print('O número \033[31m{}\033[m é maior.'.format(n2))
else:
    print('Não existe número maior, \033[33mambos são iguai\033[m.')