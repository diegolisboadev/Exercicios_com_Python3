#Dicionários Python

alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

print(alien_0)

alien_0['position_x'] = 0
alien_0['position_y'] = 25

print(alien_0)

#Dicionario vazio

dicio = {}

dicio['color'] = 'blue'
dicio['points'] = 10

print(dicio)

dicio['color'] = 'yellow'

print(dicio)

#Dicio ex 3
alien_1 = {'x_position': 1, 'y_position': 25, 'speed': 'fast'}

print(alien_1)

if alien_1['speed'] == 'slow': x_increment = 1
elif alien_1['speed'] == 'medium': x_increment = 2
else: x_increment = 3

alien_1['x_position'] += x_increment

print("Nova posição é {}".format(alien_1['x_position']))

#Removendo pares chave-valor do dicionário Python 3
print(alien_0)
del alien_0['points']
print(alien_0)

#Enquete para adicionar as linguagens favoritas de uma pessoa
linguagens_favoritas = {'jen':'python', 'sarah': 'c', 'edward':'ruby', 'phil':'python', }
print('Sarah linguagem favorita é {}'.format(linguagens_favoritas['sarah']))

#Pecorre com For o Dict
user = {'username': 'Di', 'first': 'Diego', 'last': 'Pires'}

for key, values in user.items():#O metodo items() - pegar chave e valor do dict
    print(key, values)

print('\n')
#Pecorrendo com keys() - pegando somente a chave do dict
for chave in linguagens_favoritas.keys():
    print(chave)

print('\n')

#Teste com for - dict
amigos = ['jen', 'phil']

for nomes in linguagens_favoritas.keys():
    print(nomes.title())

    if nomes in amigos:
        print('Oi seu nome é {} e sua linguagem favorita é {}'.format(nomes.title(), linguagens_favoritas[nomes].title()))

    if 'erin' not in linguagens_favoritas.keys():
        print('Erin Não participou da enquete')

#Teste Pecorrendo Dicionário com um Laço
user_3 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}

for key, value in user_3.items():
    print('\nKey:' + key)
    print('Value: ' + value.title())

print('\n=====\n')

#Teste 2 Favorite_Languages
for key in linguagens_favoritas.keys():
    print(key.title(), end='->')

print('\n=====\n')

#Teste  - ordenando o dicionario usando sorted() no for Python
for name in sorted(linguagens_favoritas.keys()):
    print(name.title())

print('\n=====\n')

#Teste 5 - pecorrendo o dict buscando somente os valores
for language in linguagens_favoritas.values():
    print(language, end=' -> ')

print('\n=====\n')

#Teste 6 - usando o conjunto set() para mostrar os dados únicos sem repetições -
#o set identificar os dados unicos e cria um conjunto em cima disso retornando dados únicos
for languages in set(linguagens_favoritas.values()):
    print(languages, end=' -> ')

print('\n=====\n')

#Lista de Dicionarios
alien_3 = {'color': 'green', 'points': 5}
alien_4 = {'color': 'yellow', 'points': 10}
alien_5 = {'color': 'red', 'points': 15}

aliens = [alien_3, alien_4, alien_5]

for a in aliens:
    print(a)


print('\n=====\n')

#Teste de lista dict 2 com range
aliens = []

for alien in range(30):
    alien_new = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien_new)

#Mostra os 30 alienigenas
print(aliens)

#Mostra os 5 pimeiros aliens
print(aliens[:5])

#Mostra a quantidade de Aliens
print('{} aliens'.format(len(aliens)))

print('\n=====\n')

#Teste 3 dict e lista python - mudando valores do dict
for al in aliens[0:3]:
    if al['color'] == 'green':
        al['color'] = 'yellow'
        al['points'] = 10
        al['speed'] = 'medium'

for alie in aliens[0:5]:
    print(alie)

print('======'*30)

for al in aliens[0:3]:
    if al['color'] == 'green':
        al['color'] = 'yellow'
        al['points'] = 10
        al['speed'] = 'medium'
    elif al['color'] == 'yellow':
        al['color'] = 'red'
        al['points'] = 15
        al['speed'] = 'fast'


for ale in aliens[:5]:
    print(ale)

print('===='*30)

#Uma lista em um dicionário
lista = ['musshrooms', 'extra_cheese'] #Implements extra
pizza = {'crust': 'thick', 'toppings': lista, }

#Resumo do pedido
print('Você pediu {} - crust pizza, com o seguinte:'.format(pizza['crust']))

for p in pizza['toppings']:
    print('\n', p)

print('====='*30)

languages_favorites = {'jen': ['python', 'go'], 'sarah': ['c'], 'edward': ['ruby', 'go'], 'phil': ['python', 'haskell'], }

for name, linguagem in languages_favorites.items():
    if len(linguagem) > 1:
        print('O(a) {} gosta das linguagens {}'.format(name.title(), str(linguagem).title().strip("[]")))
    else:
        print('O(a) {} gosta somente desta {} linguagem'.format(name.title(), str(linguagem).title().strip("[]")))

print('======='*30)

#Dict dentro de um dict
users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
        'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris',}, }

for user_name, user_info in users.items():
    print('Nome: {}'.format(user_name))
    print('Nome completo: {} {}'.format(user_info['first'], user_info['last']))
    print('Local: {}'.format(user_info['location']))
    print('\n')


