
#Exercicio 02

''''num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

soma = num1+num2

print('A soma entre {} e {} é {}'.format(num1, num2, soma))'''

#teste slicing str

import os

frase = 'C:/Users/Diego Lisboa/Desktop/300x250.jpg'

print(frase.split())

nome = os.path.basename(frase)

print(nome[:-4])