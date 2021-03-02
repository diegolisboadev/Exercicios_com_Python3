#====DESAFIO PYTHON 10 CV ====

#faça um programa que leia um valor qualquer e mostre na tela a sua tabuada
#Tabuada de Multiplicação

#Calculadora de Multiplicação de Qualquer Número

valor = int(input('Insira um valor? '))

inteiros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('='*12)

for i in inteiros:
    s = valor * i
    print('{} x {} = {}'.format(valor, i, s))

print('='*12)

    #Subtração
    #sub = valor - i
    #print('{} - {} = {}'.format(valor, i, sub))

    #Multiplicação
    #mult = valor * i
    #print('{} x {} = {}'.format(valor, i, mult))

    #Divisão
    #if i != 0:
     #   div = valor // i
      #  print('{} / {} = {}'.format(valor, i, div))


