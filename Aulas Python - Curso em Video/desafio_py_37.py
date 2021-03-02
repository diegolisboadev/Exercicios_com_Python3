#====DESAFIO PYTHON 37 CV ====

#Primeiro ou segundo maior ou são iguais (Comparando valores)

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))

if num1 > num2:
    print('O Primeiro valor {} é maior que o segundo valor {}'.format(num1, num2))
elif num2 > num1:
    print('O Segundo valor {} é maior que o primeiro valor {}'.format(num2, num1))
else:
    print('Os dois valores são iguais!!')


