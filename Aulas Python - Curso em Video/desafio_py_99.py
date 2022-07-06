
# Exercicio 99

from random import randint

def sorteia():
    lista = [randint(0, 10) for i in range(1, 6)]
    return lista

def somaPar(numeros):
    num = 0
    listPar = [ v for v in numeros if v % 2 == 0 ]
    for lp in listPar:
        num += lp
    return num

numeros = sorteia()
print(f'Sorteando {len(numeros)} valores da lista: {numeros}')

soma = somaPar(numeros)
print(f'Somando os valores pares de {numeros}, temos {soma}')