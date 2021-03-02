
#====DESAFIO PYTHON 53 CV ====

#Pega o ano de nascimento de 7 pessoas e mostre quantos já atingiram a maior idade e quantos não

from datetime import date

ano_nasc = []

ano_atual = date.today().year

for an in range(1,8):
    data_nas = int(input('Informe o ano de nascimento da {}º pessoa: '.format(an)))
    ano_nasc.append(data_nas)

for i in ano_nasc:
    if ano_atual - i > 21:
        print('Nascido no ano de {} com {} de idade, É MAIOR DE IDADE'.format(i, (ano_atual - i)))
    else:
        print('Nascido no ano de {} com {} de idade, É MENOR DE IDADE'.format(i, (ano_atual - i)))


#Segundo Modo
ano_atual = date.today().year

cont = 0
cont2 = 0

for an in range(1,8):
    data_nas = int(input('Informe o ano de nascimento da {}º pessoa: '.format(an)))
    idade = ano_atual - data_nas
    if idade >= 21:
        print('Nascido no ano de {} com {} de idade, É MAIOR DE IDADE'.format(data_nas, idade))
        cont += 1
    else:
        print('Nascido no ano de {} com {} de idade, É MENOR DE IDADE'.format(data_nas, idade))
        cont2 += 1
print('São {} maiores de idade'.format(cont))
print('São {} menores de idade'.format(cont2))