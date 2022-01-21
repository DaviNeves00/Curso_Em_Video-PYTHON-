'''
DESAFIO 45
Faça um programa que jogue jokempô com você
'''
import random
jogo = [
    'pedra', 'tesoura', 'papel'
]
pc = random.choice(jogo)
user = str(input('Vamos jogar \033[30;43mjokempô\033[m. Escolha: \033[33mPEDRA\033[m, \033[33mPAPEL\033[m ou \033[33mTESOURA\033[m: '))
if pc == 'pedra' and user == 'tesoura':
    print('Eu escolhi \033[31mpedra\033[m, GANHEI!!!')
elif pc == 'pedra' and user == 'papel':
    print('Parabéns. Eu escolhi \033[31mpedra\033[m, você venceu.')
elif pc == 'tesoura' and user == 'papel':
    print('Eu escolhi \033[31mtesoura\033[m, GANHEI!!!')
elif pc == 'tesoura' and user == 'pedra':
     print('Parabéns. Eu escolhi \033[31mtesoura\033[m, você venceu.')
elif pc == 'papel' and user == 'pedra':
    print('Eu escolhi \033[31mpapel\033[m, GANHEI!!!')
elif pc == 'papel' and user == 'tesoura':
    print('Parabéns. Eu escolhi \033[31mpapel\033[m, você venceu.')
elif pc == user:
    print('Eu também escolhi \033[31m{}. Quer jogar outra?'.format(user))
else:
    print('\033[30;41mJOGA DIREITO, DESGRAÇA.\033[m')