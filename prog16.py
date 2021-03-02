#Programa 16 Curso Intensivo Python

#exerc 16

pessoas_jantar = ['Luane', 'Lucas', 'Rosidete']

print('Quer jantar comigo {}'.format(pessoas_jantar[0]))
print('Quer jantar comigo {}'.format(pessoas_jantar[1]))
print('Quer jantar comigo {}'.format(pessoas_jantar[2]))

#Não poderá comparecer
print('{} pediu desculpas pois, não poderá comparecer'.format(pessoas_jantar.pop(1)))

#Novo Convite
pessoas_jantar.insert(1, 'Riba')
print('Então convidei {}'.format(pessoas_jantar[1]))

#Nova lista de convites
print('Quer jantar comigo {}'.format(pessoas_jantar[0]))
print('Quer jantar comigo {}'.format(pessoas_jantar[1]))
print('Quer jantar comigo {}'.format(pessoas_jantar[2]))

#Adicionando novos convidados em pontos diferentes da lista
pessoas_jantar.insert(0, 'Maria')
pessoas_jantar.insert(2, 'Luna')
pessoas_jantar.append('Edileuza')

print('Encontrei uma mesa de jantar maior, Quer jantar comigo {}'.format(pessoas_jantar[3]))
print('Encontrei uma mesa de jantar maior, Quer jantar comigo {}'.format(pessoas_jantar[4]))
print('Encontrei uma mesa de jantar maior, Quer jantar comigo {}'.format(pessoas_jantar[5]))

print(pessoas_jantar)

#Mesa só é permitida para duas pessoas
print('Eita!! Desculpem só posso convidar duas pessoas :/')

print('Desculpe!! não posso convidá-la(o) para jantar {}'.format(pessoas_jantar.pop(0)))
print('Desculpe!! não posso convidá-la(o) para jantar {}'.format(pessoas_jantar.pop(2)))
print('Desculpe!! não posso convidá-la(o) para jantar {}'.format(pessoas_jantar.pop(3)))
print('Desculpe!! não posso convidá-la(o) para jantar {}'.format(pessoas_jantar.pop(1)))

#Ultimos dois convidados
print('{} você ainda está convidada(o)'.format(pessoas_jantar[0]))
print('{} você ainda está convidada(o)'.format(pessoas_jantar[1]))

#Removendo todos os convidados da lista
#del pessoas_jantar #deve ser usado na questão

#clear() limpar a lista
pessoas_jantar.clear()

print(pessoas_jantar)

