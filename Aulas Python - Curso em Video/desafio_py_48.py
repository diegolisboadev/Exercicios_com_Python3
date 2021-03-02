
#====DESAFIO PYTHON 47 CV ====

#Criar uma tabuada usando laço for

print('{:=^40}'.format(' TABUADA '))

num = int(input('Escolha um número: '))

print('''Escolha a tabuada:
        (1) SOMA
        (2) SUBTRAÇÃO
        (3) MULTIPLICAÇÃO
        (4) DIVISÃO''')
escolha = int(input('Qual sua opção: '))

if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
    print('\033[0;33mOPS!! Valor inválido!!! Informe entre 1 e 4.\033[m')
else:
    for x in range(0, 11):
        if escolha == 1:
            print('{} + {} = {}'.format(num, x, (num + x)))
        elif escolha == 2:
            print('{} - {} = {}'.format(num, x, (num - x)))
        elif escolha == 3:
            print('{} x {} = {}'.format(num, x, (num * x)))

if escolha == 4:
    for x in range(1,10):
        print('{} / {} = {}'.format(num, x, (num // x)))