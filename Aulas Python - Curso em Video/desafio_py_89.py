
# Exercicio 89

nome = input('Informe seu nome do aluno: ')
media = float(input(f'Informe a Média de {nome} aluno: '))

situacao = None
if(media >= 7):
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

dict_aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print(f'Nome é igual a {dict_aluno["nome"]}')
print(f'Média é igual a {dict_aluno["media"]}')
print(f"Situação é igual a {dict_aluno['situacao']}")