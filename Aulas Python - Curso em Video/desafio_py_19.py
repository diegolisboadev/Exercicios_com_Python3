
#====DESAFIO PYTHON 19 CV ====

#Sorteio de Alunos para a apresentação dos trabalhos

from random import shuffle

nomes = []

#Inserindo os dados no Array
for n in range(4):
    nome = input('Digite o nome do Aluno: ')
    nomes.append(nome)

print('Os nomes dos Alunos são: {}'.format(nomes))

#Selecionando a ordem de apresentação - shuffle() embaralhar a lista

shuffle(nomes)

print('O Ordem para apresentação dos trabalhos é {}'.format(nomes))