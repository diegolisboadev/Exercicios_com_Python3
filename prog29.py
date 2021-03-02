#Laço While e Entrada de Usuários
#Exercio 2

from time import sleep

#Atividade 1
'''ingre = ''

while ingre != 'quit':
    ingre = input('Ingrediente da Pizza: ')

    if ingre == 'quit':
        break

    print('Iremos acrescentar o ingrediente {}'.format(ingre.capitalize()))'''

#Atividade 2

'''while True:
    idade = int(input('Qual sua idade? '))

    if idade < 3:
        print('Ingresso gratuito!')
    elif 12 >= idade >= 3:
        print('Ingresso 10 reais')
    elif idade > 12:
        print('Ingresso 15 reais')
    else:
        break'''

#Atividade 3
'''cont = 0
while True:
    print(cont)
    cont += 1'''

#Aula Exemplos
'''animais = ['dog', 'cat', 'fish', 'bol', 'cat', 'pulma', 'cat']

while 'cat' in animais:
    animais.remove('cat')

print(animais)'''


#Atividade 3 (1)

'''sandwich = ['atum', 'carne de porco', 'frango', 'toscana', 'salsicha', 'cane de bovina']

finish_sandwich = []

for sand in sandwich:
    print("Preparei seu sandwich de {}".format(sand))
    finish_sandwich.append(sand)

for fs in finish_sandwich:
    print("Terminando...")
    sleep(3)
    print('O sandwich {} está preparado!'.format(fs))'''

#Atividade 3 (2)

'''sandwich = ['atum', 'carne de porco', 'frango', 'toscana', 'salsicha', 'pastrami', 'pastrami',
            'pastrami']

finish_sandwich = []

print("A lanchonete está sem Pastrami.")

while 'pastrami' in sandwich:
    sandwich.remove('pastrami')

for sand in sandwich:
    print("Preparei seu sandwich de {}".format(sand))
    finish_sandwich.append(sand)

for fs in finish_sandwich:
    print("Terminando...")
    sleep(3)
    print('O sandwich {} está preparado!'.format(fs))'''

#Atividade 3 (3)

#Enquete Férias

enquete_ferias = {}
nome = ''
quest = ''
ativo = True

while True:
    nome = input("Informe seu Nome: ")
    quest = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    sair = input("Deseja sair da enquente? [S]/[N]").lower()
    enquete_ferias[nome] = quest

    if sair == 's':
        ativo = False
        break


for fs in enquete_ferias.items():
    print("Aguarde enquanto trazemos os resultados da enquete...")
    sleep(3)
    print("O (a) {} disse que queria viajar para {}.".format(nome, quest))