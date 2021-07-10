

# Exercicio 93 py
from functools import reduce

lista_pessoas = []
pessoas = dict()

while True:
    pessoas['nome'] = input('Informe seu nome: ').capitalize()
    pessoas['sexo'] = input('Informe seu sexo [M | F]: ').upper()
    pessoas['idade'] = int(input('Informe sua idade: '))

    lista_pessoas.append(pessoas.copy()) # Adiciono uma cópia do dicionário pessoas
    pessoas.clear() # Limpo o dicionário pessoas para adicionar novos dados

    opcao = input('Deseja continuar cadastrando? [S | N] ') 
    if opcao.lower() == 'n': break


# Letra A
print(f'Foram cadastradas {len(lista_pessoas)} pessoas!')

# Letra B
media_idade = [lista_pessoas[chave]['idade'] for chave, pessoa in enumerate(lista_pessoas)]
media_idade = sum(media_idade) / len(lista_pessoas) # Divisão retorno com ponto flutuante
print(f'A média de idade do grupo é: {media_idade}')

# Letra C
mulheres = [m for chave, m in enumerate(lista_pessoas) if lista_pessoas[chave]['sexo'] == 'F']
mulheres = [lista_pessoas[chave]['nome'] for chave, nome in enumerate(lista_pessoas) ]
print(f'As mulheres são: {mulheres}')

# Letra D 
pessoas_acima_media = [pessoa for chave, pessoa in enumerate(lista_pessoas) if lista_pessoas[chave]['idade'] > media_idade]
print(f'Pessoas com a idade acima da média {media_idade}: {pessoas_acima_media}')