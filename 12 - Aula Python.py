
#Aula 12 Python

#Cores no Terminal
#Dá um olhada no módulo colorysys

print('\033[4;30;43mOlá Mundo!!!\033[m')
print('\033[4;30;45mOlá Mundo!!!\033[m')
print('\033[7;30mOlá Mundo!!!\033[m')
print('\033[7;33;44mOlá mundo!!!\033[m')

a = 5
b = 3

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Diego'
cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;30m'}

print('Olá muito prazer em te conhecer, {}{}{}'.format('\033[4;34m', nome,'\033[m'))

print('Olá muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome,cores['limpa']))