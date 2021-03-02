
#Programa 23 Curso Intensivo Python

#exerc 23

lista = ['folha', 'papel', 'livro', 'caderno', 'regua']

print('Os 3 primeiros itens da lista são: {}'.format(lista[:3]))

print('Os 3 itens do meio da lista são: {0}'.format(lista[1:4]))

print('Os 3 ultimos itens da lista são: {0}'.format(lista[-3:]))

#exerc 2

pizza = ['mussarela', 'frango cautpiry', 'portuguesa', 'napolitana']

amigos_pizza = pizza[:]#copia da list pizza

pizza.append('adocicada')

amigos_pizza.append('salgada')

print('Minhas pizzas favoritas são: {}'.format(pizza))
for ls in lista:
    print(ls)

print('As pizzas favoritas do meu amigo são: {}'.format(amigos_pizza))
for lst in amigos_pizza:
    print(lst)

#exibindo a lista de comidas (pizzas)
for lt in lista:
    print(lt)

for tl in amigos_pizza:
    print(tl)






