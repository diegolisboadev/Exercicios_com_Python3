
#Programa 27 Curso Intensivo Python

#exerc 27

lista = ['admin', 'supervisor', 'chefe', 'funcionario']

'''for l in lista:
    if l == 'admin':
        print('Olá, {} gostaria de ver um relatório de status!!'.format(l))
    else:
        print('Olá, {} obrigado por fazer login novamente!!'.format(l))'''

'''if lista:
    for ls in lista:
        if ls == 'admin':
            print('Olá, {} gostaria de ver um relatório de status!!'.format(ls))
        else:
            print('Olá, {} obrigado por fazer login novamente!!'.format(ls))
else:
    print('Precisamento encontrar alguns usuários.')'''


#exerc3

'''usuarios = ['maria', 'sergio', 'admin', 'mario', 'paulo', 'lucas', 'maria']

novos_usuarios = ['LUCAS', 'cecilia', 'luane', 'marcos', 'gabriel']

for nu in novos_usuarios:
    if nu.lower() in str(usuarios).lower():
        print('Ops {}! Nome em uso, forneça um novo nome de usuário!!'.format(nu))
    else:
        print('Nome {} disponivel'.format(nu))'''

#exer4

lista_ordinais = [1,2,3,4,5,6,7,8,9]

for lo in lista_ordinais:
    if lo == 1:
        print('{}st'.format(lo))
    elif lo == 2:
        print('{}nd'.format(lo))
    elif lo == 3:
        print('{}rd'.format(lo))
    else:
        print('{}th'.format(lo))





