
#====DESAFIO PYTHON 51 CV ====

#Numero inteiro é ou não primo

num = int(input('Insira o número: '))

primos = []
cont = 0

#Divisor: se o resto da divisão do número informado por outro número for igual a 0 é divisor
#Primeiro listar o números primos
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        primos.append(i)


if len(primos) > 2:
    print('O número {} foi divisível {} vezes - NÃO É PRIMO!!'.format(num, cont))
elif len(primos) == 2:
    print('O número {} foi divisível {} vezes - É PRIMO!!'.format(num, cont))

