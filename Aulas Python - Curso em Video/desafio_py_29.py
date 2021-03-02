#====DESAFIO PYTHON 29 CV ====

#Par ou Impar em Python

from time import sleep

num = int(input('Informe um número: '))

print('Verificando...')
sleep(5)

if num % 2 == 0:
    print('O número {} é um número PAR!'.format(num))
else:
    print('O número {} é um número IMPAR!!'.format(num))

#Forma simplificada de fazer a condição com if e else (parece ternário mais não é)
#print('O número é PAR!' if num % 2 == 0 else 'O número é IMPAR!')
