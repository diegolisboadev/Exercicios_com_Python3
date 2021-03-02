>>> #Operações com Listas
>>> lista = [1,2,3,4,5]
>>> lista.append(6)
>>> lista
[1, 2, 3, 4, 5, 6]
>>> lista.insert(0, -1)
>>> lista
[-1, 1, 2, 3, 4, 5, 6]
>>> lista.remove(6)
>>> lista
[-1, 1, 2, 3, 4, 5]
>>> lista.pop(0)
-1
>>> lista
[1, 2, 3, 4, 5]
>>> lista.reverse()
>>> lista
[5, 4, 3, 2, 1]
>>> lista.sort()
>>> lista
[1, 2, 3, 4, 5]
>>> lista.index(5)
4
>>> lista2 = [6,7,8,9,10]
>>> lista.extend(lista2)
>>> lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lista.clear()
>>> lista
[]
>>>

#Demais Operações com Listas

>>> bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
>>> bicicletas
['trek', 'cannondale', 'redline', 'specialized']

#Imprimindo listas com Slice Notation - pegando o indice no trilho da lista
>>> print(bicicletas[0:3])
['trek', 'cannondale', 'redline']
>>> print(bicicletas[0])
trek

#Usando funções string com listas
>>> print(bicicletas[0].title())
Trek
>>> print(bicicletas[1:3])
['cannondale', 'redline']
>>> print(bicicletas[0], bicicletas[3])
trek specialized

#Pegando o último valor da lista
>>> print(bicicletas[-1])
specialized

#Pegando o tamanho da lista
>>> len(bicicletas)
4

#Substituindo o valor de um elemento na lista pegando o indice

>>> bicicletas[4] = 'Correr'
>>> bicicletas[1] = 'Correr'
>>> bicicletas
['trek', 'Correr', 'redline', 'specialized']
>>> motocicletas = ['honda', 'yamaha', 'suzuki']
>>> motocicletas
['honda', 'yamaha', 'suzuki']
>>> motocicletas[0] = 'ducati'
>>> motocicletas
['ducati', 'yamaha', 'suzuki']

#Adicionando um elemento na lista com append() - concatenação
>>> motocicletas.append('kawasaki')
>>> motocicletas
['ducati', 'yamaha', 'suzuki', 'kawasaki']

#Passando um dados para a lista atraves do append() - concatenação

>>> motocycles = []
>>> motocycles.append('Honda')
>>> motocycles.append('yamaha')
>>> motocycles.append('suzuki')
motocycles['Honda', 'yamaha', 'suzuki']

#Continuação do ensinamento de lista

>>> motorcycles = ['honda', 'yamaha', 'suzuki']

#Inserindo dados na lista passando o indice e o valor - insert(indice, valor)

>>> motorcycles.insert(3, 'kawasaski')
>>> motorcycles
['honda', 'yamaha', 'suzuki', 'kawasaski']

#Removendo um elemento permanentemente da lista com del

>>> del motorcycles[0]
>>> motorcycles
['yamaha', 'suzuki', 'kawasaski']
>>> motorcycles[0]
'yamaha'
>>> motorcycles
['honda', 'yamaha', 'suzuki', 'kawasaski']
>>> motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaski']

#Removendo o ultimo elemento da lista e posteriormente tendo a possibilidade de
#usá-lo com pop()

>>> motorcycles_pop = motorcycles.pop()
>>> motorcycles_pop
'kawasaski'
>>> motorcycles
['honda', 'yamaha', 'suzuki']

#Removendo elemento definido com pop() passando um indice como argumento
>>> motorcycles_pop = motorcycles.pop(0)
>>> motorcycles_pop
'honda'
>>> motorcycles
['yamaha', 'suzuki']
>>> motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaski']
>>> last_owned = motorcycles.pop()
>>> print('Última moto comprada por mim {}'.format(last_owned))
Última moto comprada por mim kawasaski
>>> motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

#Removendo um elemento da lista passando o valor um argumento como argumento no remove()

>>> moto_remove = motorcycles.remove('honda')
>>> moto_remove
>>> motorcycles
['yamaha', 'suzuki', 'ducati']
>>> motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
>>> moto_ext = 'ducati'
>>> motorcycles.remove(moto_ext)

#Motrando o elemento excluido após se destituido da lista

>>> print('A'+moto_ext.title()+'e também expensiva pra mim!!')
ADucatie também expensiva pra mim!!

#Continuando a Aula de Listas
>>> cars = ['bmw','audi','toyota','subaru']
>>> cars
['bmw', 'audi', 'toyota', 'subaru']

#Ordenando a lista em ordem alfabética permanentemente
>>> cars.sort()
>>> cars
['audi', 'bmw', 'subaru', 'toyota']
>>> cars = ['bmw','audi','toyota','subaru']

#Ordenando a lista em ordem alfabetica porém reversa reverse=True permanentemente
>>> cars.sort(reverse=True)
>>> cars
['toyota', 'subaru', 'bmw', 'audi']
>>> cars.sort()
>>> cars
['audi', 'bmw', 'subaru', 'toyota']
>>> cars.sort(reverse=True)
>>> cars
['toyota', 'subaru', 'bmw', 'audi']
>>> cars = ['bmw','audi','toyota','subaru']

#Ordenando a lista temporariamente na memória
>>> sorted(cars)
['audi', 'bmw', 'subaru', 'toyota']
>>> cars
['bmw', 'audi', 'toyota', 'subaru']
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> cars
['bmw', 'audi', 'toyota', 'subaru']

#Revertendo a ordem da lista reverse() permanentemente
>>> cars.reverse()
>>> cars
['subaru', 'toyota', 'audi', 'bmw']

#Voltando a ordem orginal com reverse novamente
>>> cars.reverse()
>>> cars
['bmw', 'audi', 'toyota', 'subaru']

#Verificando o tamanho da lista
>>> len(cars)
4

#Iterando listas com for em Python

magicos = ['alice', 'david', 'carolina']
for m in magicos:
    print(m)


for magico in magicos:
    print('Parabéns {} pelo truque!!'.format(magico.title()))

for magico in magicos:
    print('Parabéns {} pelo truque!!'.format(magico.title()))
    print('Estamos ansioso pelo seu próximo truque!!')
magicos = ['alice', 'david', 'carolina']

for magico in magicos:
    print('Parabéns {} pelo truque!!'.format(magico.title()))
    print('Estamos ansioso pelo seu próximo truque!!')

print('Obrigado Mágicos pelo execelente show!!!')

#Listas Númericas em Python

for value in range(1, 5):
    print(value)

1
2
3
4
for value in range(1, 6):
    print(value)

1
2
3
4
5
for value in range(5):
    print(value)

0
1
2
3
4
# Lista de uma sequencia de números - transformando um range() em um list()
for value in list(range(10)):
    print(value)

0
1
2
3
4
5
6
7
8
9
numbers = list(range(10))
print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_par = list(range(2, 11, 2))
print(num_par)
[2, 4, 6, 8, 10]
num = list(range(1, 6))
print(num)
[1, 2, 3, 4, 5]



squares = []

for value in range(1,11):
    #square = value **2
    squares.append(pow(value, 2)) #square

print(squares)

#Menor número, maior número e soma dos valores de uma lista

lista = [1,2,3,4,5,6,7,8,9,0]

print(min(lista))
print(max(lista))
print(sum(lista))

#Usando list comprehensions (abrangência de lista)

square = [pow(value, 2) for value in range(1,11)]
print(square)


#Fatiamento de lista
players = ['charles', 'marina', 'michael', 'florence', 'eli']


print(players[0:3])#slice notation python
print(players[1:4])
print(players[:4])
print(players[2:])

#Dependendo do valor negativo ele me retorna o elemento em ordem descrescente
print(players[-1:])#apresentar os ultimo jogador da lista
print(players[-3:])#apresentar os 3 ultimos jogadores da lista
print(players[-2])#apresentar o penultimo jogador da lista

print('='*30)

#Percorre uma fatia da lista em Python

for l in players[:3]:
    print(l.title())

print('='*30)

#Copiando uma lista

comidas = ['pizza', 'bolo', 'salgado']

amigos = comidas[:]#copiando minha lista para outra

print(amigos)

comidas.append('macarronada')
amigos.append('doce')

print(comidas)
print(amigos)

#Modo incorreto de copiar uma lista (no caso aqui a lista2 está apontando a lista sendo igual a ela)
lista = ['nome', 'sobre', 'about']

lista2 = lista

lista2.append('legal')

print(lista2)
print(lista)

#Modo correto de copia de lista
lista2 = lista[:]#usando slice notation
