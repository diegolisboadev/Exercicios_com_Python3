#Dicionarios

#1 Exercicio

pessoa = {'firstname': 'Paulo', 'lastname': 'Sousa', 'age': 24, 'city':'São Luis'}

print(pessoa['firstname'])
print(pessoa['lastname'])
print(pessoa['age'])
print(pessoa['city'])

#Exercicio 2
numeros_favoritos = {'Maria': 2, 'Diego': 3, 'Filipe': 7, 'Luane': 5, 'Mario': 9}

for key, value in numeros_favoritos.items():
    print(key, ' - ', value)

#Exercicio 3
glossario = {'python': 'Linguagem de programação interpretada que pode ser utilizada com diferentes\n'
                       'paradigmas como Orientação a Objeto, Funcional e Estruturado',
             'listas': 'Um tipo de estrutura de dados em Python mutavel',
             'identação': 'Formatar seu código no padrão correto para a linguagem',
             'pip': 'Packages Imports Python, pacotes de bibliotecas da Linguagem Python',
             'print': 'Funçaõ para imprimir alguma texto ou objeto em python'}

for key, value in glossario.items():
    print(key, ': ', value)
    print(' == ')

print('\n=====\n')

#Exercicio 1 - new
glossario2 = {'python': 'Linguagem de programação interpretada que pode ser utilizada com diferentes\n'
                       'paradigmas como Orientação a Objeto, Funcional e Estruturado',
             'listas': 'Um tipo de estrutura de dados em Python mutavel',
             'identação': 'Formatar seu código no padrão correto para a linguagem',
             'pip': 'Packages Imports Python, pacotes de bibliotecas da Linguagem Python',
             'print': 'Funçaõ para imprimir alguma texto ou objeto em python',
             'set': 'Criar um conjunto unico de strings - strings unicas sem repetiçoes',
             'sorted()': 'Ordenar dados iteraveis',
             'match()': 'Função para regex python',
             'for': 'Laço foreach python - iterar dados'}

for chave, valor in glossario2.items():
    print('Key:' + chave + '\nValue:' + valor)

print('\n=====\n')

#Exercio dict rios e locais
rios = {'nilo': 'egito', 'tamisa': 'paris', 'amazonas': 'brasil'}

for c, v in rios.items():
    print('O rio {} corre em {}'.format(c, v))

print('\n=====\n')

#For cada país do onde o rio corre
for p in rios.values():
    print(p)

print('\n=====\n')

#Exercio 5 nova favorite_languages
new_persons = ['diego', 'luzia', 'fabio', 'lucio', 'jen', 'sarah']

linguagens_favoritas = {'jen':'python', 'sarah': 'c', 'edward':'ruby', 'phil':'python',}

for e in new_persons:
    if e in linguagens_favoritas:
        print('Obrigado {} por responder a enquete'.format(e.title()))
    else:
        print('Por favor {} responda a enquete'.format(e.title()))

print('====='*30)

#Exercicio 4 - atividade 1
usuario1 = {'nome_completo': 'Paulo Silva Lima', 'cidade': 'São Luis', 'estado': 'MA',}
usuario2 = {'nome_completo': 'Maria Sousa', 'cidade': 'Barreirinhas', 'estado': 'MA',}
usuario3 = {'nome_completo': 'Saulo Lima', 'cidade': 'São Paulo', 'estado': 'SP'}

people = [usuario1, usuario2, usuario3]

for l in people:
    print('O(a) {} mora na cidade de {} e no estado de {}'.format(l['nome_completo'], l['cidade'], l['estado']))

print('======'*30)

#Exercicio 4 - atividade 2
paco = {'tipo_animal': 'Papagaio', 'nome_dono': 'Mario'}
rosa = {'tipo_animal': 'Coruja', 'nome_dono': 'Diego'}
simba = {'tipo_animal': 'Gato', 'nome_dono': 'Luane'}
dog = {'tipo_animal': 'Cachorro', 'nome_dono': 'Silvia'}

pets = [paco, rosa, simba, dog]

for p in pets:
    print('O(a) {} é dono de um {}'.format(p['nome_dono'], p['tipo_animal']))

print('===='*30)

#Exercicio 4 - atividade 3
'''favorite_places = {'diego': {'paris', 'jalapão', 'barreirinhas', },
                   'maria': {'rio', 'africa', 'italia', },
                   'paulo': {'manaus', 'são paulo', 'dunas'}, }

favorite_places['diego'] = input('Informe outros 3 lugares {}: '.format('Diego'))
favorite_places['paulo'] = input('Informe outros 3 lugares {}: '.format('Paulo'))

print(favorite_places)'''

print('===='*30)

#Exercicio 4 - atividade 4
num_favoritos = {'Maria': {2, 3, 6, 8, } ,
                 'Diego': {3, 1, 0, 6, 7, } ,
                 'Filipe': {7, 2, 5, 8, 10, } ,
                 'Luane': {5, 3, 1, 6, 0, } ,
                 'Mario': {9, 0, 8, 2, 1, }, }

for p, n in num_favoritos.items():
    print('A pessoa {} tem os números {} como favoritos!'.format(p, n))


print('===='*30)

#Exercicio 4 - atividade 5
cities = {'sao paulo': {'country': 'brasil', 'population': '10.000', 'fact': 'maior da america latina', },
          'londres': {'country': 'italia', 'population': '50.000', 'fact': 'linda', },
          'madrid': {'country': 'espanha', 'population': '100.000', 'fact': 'bela', }, }

for c in cities.keys():
    print('A cidade {} do {} tem aproximadamente {} pessoas, sendo {}'.format(c, cities['sao paulo']['country'],
                                                                        cities['sao paulo']['population'],
                                                                              cities['sao paulo']['fact']))

