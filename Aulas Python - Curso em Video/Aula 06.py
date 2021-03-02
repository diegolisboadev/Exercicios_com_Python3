
# TUPLAS CURSO EM VIDEO MUNDO 3

tupla = "ok"
tuplas = 'ok','1','3','4' # OBS. tuplas são imutáveis
# A partir do python 3.5 você pode criar uma tupla sem parenteses
print(tupla)
print(tuplas[1:])
# tuplas[2] = "lista"
print(len(tuplas))
for pos, c in enumerate(sorted(tuplas)):
    print(c, pos)
lista = []
dicionario = {}

a = (2, 5, 4)
b = (5, 8, 2, 1)
c = a + b
print(a+b)
print(set(a+b))
print(c.count(5))
print(c.index(5))
print(c.index(5, 1))
del(tuplas) # deletar toda a tuplas da memória (vale também para - listas e dicionários)