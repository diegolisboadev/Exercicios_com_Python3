#Programa 17 Curso Intensivo Python

#exerc 17

lugares = ['Rússia', 'Chile', 'Londres', 'Holanda', 'Japão']

print(lugares)

print('='*50)

#Usando sorted() para exibir a lista temporariamente
print(sorted(lugares))

print('='*50)

#Ordem original da lista
print(lugares)

print('='*50)

#Ordem inversa da lista em ordem alfabetica temporariamente
print(sorted(lugares, reverse=True))

print('='*50)

#Ordem original da lista
print(lugares)

print('='*50)

#Mudando a ordem da lista com reverse() permanentemente
lugares.reverse()
print(lugares)

print('='*50)

#Ordem original da lista com reverse()
lugares.reverse()
print(lugares)

print('='*50)
#Lista em ordem alfabética com sort()
lugares.sort()
print(lugares)

print('='*50)
#Lista modo inverso
lugares.sort(reverse=True)
print(lugares)
