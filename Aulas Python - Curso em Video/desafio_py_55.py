
#====DESAFIO PYTHON 56 CV ====

#Ler nome, idade e sexo de 4 pessoas e mostre (CODIGO GUANABARA)

somaIdade = 0
nomeHomemVelho = None
mIdadeHomem = 0
mIdadeMulher = 0

for p in range(1,5):
    print('=== {} PESSOA==='.format(p))
    nome = str(input('{} Informe seu nome: '.format(p))).strip()
    idade = int(input('{} Informe sua idade: '.format(p)))
    sexo = str(input('{} Informe seu sexo [M/F]: '.format(p))).strip()
    somaIdade += idade

    #Verificação de Homem mais velho
    if p == 1 and sexo in 'Mm':
        nomeHomemVelho = nome
        mIdadeHomem = idade
    if sexo in 'Mm' and idade > mIdadeHomem:
        nomeHomemVelho = nome
        mIdadeHomem = idade

    #Verificação para mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mIdadeMulher += 1

#A Média do grupo (idade)
print("A Média de idade do grupo é {:.2f}".format(somaIdade / 5))

#Nome do homem mais velho
print("O Homem mais velho é {} com {} de idade".format(nomeHomemVelho, mIdadeHomem))

#Quantas mulheres tem menos de 20 anos
print("A Quantidade de mulheres com menos de 20 anos é {}".format(mIdadeMulher))
