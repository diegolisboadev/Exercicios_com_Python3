
#====DESAFIO PYTHON 18 CV ====

#Sorteio de Alunos para Apagar o Quadro Negro

from random import choice

nomes = []

#Inserindo os dados no Array
for n in range(4):
    nome = input('Digite o nome do Aluno: ')
    nomes.append(nome)

print('Os nomes dos Alunos são: {}'.format(nomes))

#Selecionando o nome do Aluno Aleatoriamente (choice() escolha 1)
nome_aleatorio = choice(nomes)

print('O Nome selecionado foi: {}'.format(nome_aleatorio))

