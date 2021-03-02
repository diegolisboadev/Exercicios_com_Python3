
#Estruturas condicionais if e else em Python

tempo = int(input('Qual o ano do seu carro? '))

if tempo <= 3:
   print('Carro novo')
else:
   print('Carro velho')

print('fim')

#Operação simplificada
print('carro novo' if tempo <= 3 else 'carro velho')

print('fim')

#Estruturas condicionais if e else pt.2

carros = ['audi', 'bmw', 'subaru', 'toyota']

'''for car in carros:

    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())'''

request = 'peixe'

'''if request != 'anchovas':
    print('Não anchovas')'''

'''ingredientes = ['mushrooms', 'onions', 'peperroni']

print('mushrooms' in ingredientes)
print('onions' in ingredientes)'''

users_banned = ['carlos', 'livia', 'marcio']

if 'carlos' not in users_banned:
    print('Banida')

idade = 18

if idade >= 18:
    print('Pode votar')

#Listas com if
tipos_pizzas = ['mushrooms', 'green_peppers', 'extra_cheese']

for tp in tipos_pizzas:
    if tp == 'green_peppers':
        print('Desculpe, estamos sem pepinos!!')
    else:
        print('Adicionando {}.'.format(tp))


pizzas = []

if pizzas:
    for p in pizzas:
        print('A pizza {} foi adicionada!!'.format(p))
else:
    print('Você realmente quer uma pizza simples?')



available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for r in requested_toppings:
    if r in available_toppings:
        print('Adicionado {}'.format(r))
    else:
        print('Desculpe, não temos {}'.format(r))
print('Obrigado!!')