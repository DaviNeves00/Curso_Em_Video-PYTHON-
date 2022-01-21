'''
DESAFIO 44
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Olá, qual o valor do produto?: R$'))
pagar = str(input('Qual a forma de pagamento?: '))
des = valor * 10 / 100
des1 = valor * 5 / 100

avista = valor - des
avista1 = valor - des1
x2 = valor
x3 = valor + valor * 20 / 100

if pagar == 'dinheiro' or pagar == 'cheque':
    print('O total à pagar é: \033[32mR${:.2f}\033[m.'.format(avista))
elif pagar == 'débito no cartão' or pagar == 'debito no cartao':
    print('O total à pagar é: \033[32mR${:.2f}\033[m.'.format(avista1))
elif pagar == 'duas vezes no cartão' or pagar == '2x no cartão' or pagar == 'duas vezes no cartao' or pagar == '2x no cartao':
    print('O total à pagar é: \033[32mR${:.2f}\033[m.'.format(x2))
else:
    print('O total à pagar é: \033[32mR${:.2f}\033[m.'.format(x3))