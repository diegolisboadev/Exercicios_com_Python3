
# Exercicio 99
# TODO

from pprint import pprint
from random import randint, random, randrange

def sorteios(lista):
    lista = [randint(0, i) for i in range(6)]
    return lista

def somaPar(numeros):
    soma = []
    num = 0
    for v in numeros:
        if v % 2 == 0:
            num += v
            soma.append(num)

    return soma, num

numeros = []
numeros = sorteios(numeros)
print(numeros)

soma, num = somaPar(numeros)

pprint(num)
pprint(soma)