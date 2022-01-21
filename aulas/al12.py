#condições aninhadas

nome = str(input('Olá, qual é o seu nome?: ')).title()
print('Belo nome o seu!')

oi = str(input('Tudo bem com você, {}?: '.format(nome)))
if oi == 'sim' or oi == 'claro':
    print('Que bom!!! Aprovite o seu dia, {}!'.format(nome))
elif oi == 'nao' or oi == 'não':
    print('Não fique triste {}, a vida é feita de momentos bons e ruins. Pode ter certeza que isso irá passar!'.format(nome))
&
