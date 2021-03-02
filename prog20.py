#Programa 20 Curso Intensivo Python

#exerc 20

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