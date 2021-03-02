#====DESAFIO PYTHON 36 CV ====

#Conversão de valores para bases numéricas

num = int(input('Informe um número: '))

print('Escolhar a base de conversão desse número '
                 '\n1 - BINÁRIO\n'
                 '2 - OCTAL\n'
                 '3 - HEXADECIMAL\n')
base = int(input('Digite a sua opção: '))

if base == 1:
    print('A base em binário de {} é {}'.format(num, bin(num)[2:]))

elif base == 2:
    print('A base em octal de {} é {}'.format(num, oct(num)[2:]))

elif base == 3:
    print('A base em hexadecimal de {} é {}'.format(num, hex(num)[2:]))

else:
    print('Você informou um número inválido!!')