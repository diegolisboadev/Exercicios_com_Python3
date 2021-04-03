
# Aula 006
# Variaveis Compostas Listas

lista = []
lista.append('Diego')
lista.append(30)

galera = []
galera.append(lista[:])
lista[0] = 'José'
lista[1] = 19
galera.append(lista[:])
# print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'Nome: {p[0]} --- Idade: {p[1]}')

galera = []
dado = []

for c in range(3):
    dado.append(input('Nome: '))
    dado.append(input('Idade: '))
    galera.append(dado[:])
    dado.clear()

print(galera)