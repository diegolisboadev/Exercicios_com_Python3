#Atividades

#Atividade 1

'''def display_messages():
    print("Estou aprendendo sobre funções, parametros e argumentos")


display_messages()

#Atividade 2

def favorite_book(title):
    print("Um dos meus livros favoritos é {}".format(title))


titulo = input("Informe seu livro favorito: ")

favorite_book(titulo)'''

#Exercicio 2
#Atividade 1

'''def make_shirt(tam_camisa, msg_camisa):
    print("O tamanho da camisa é {} e a mensagem da estampa é {}!!".format(tam_camisa, msg_camisa.title()))

#Argumentos Posicionais
make_shirt(10.5, "python show")

#Argumentos Nomeados
make_shirt(msg_camisa="Olá", tam_camisa=5)'''

#Atividade 2

def make_shirt(tam_camisa=10, msg_camisa="Eu amo Python"):
    print("O tamanho da camisa é {} e a mensagem da estampa é {}!!".format(tam_camisa, msg_camisa.title()))

make_shirt(5)
make_shirt(20)
make_shirt(2, "I love Python!")

#Atividade 3

def describe_city(nome_cidade, pais="Brasil"):
    print("{} está localizada em {}".format(nome_cidade, pais))

describe_city("São Luis")
describe_city(nome_cidade="Porto Velho")
describe_city("Bruxelas", "Bélgica")

print("="*30)

#Atividade 4
""" devolvendo nome de cidades """
def city_country(cidade, pais):
    print("{}, {}".format(cidade.title(), pais.title()))

#chamadas
city_country('paris', 'frança')
city_country('brasilia', 'brasil')
city_country('manuas', 'brasil')

print("="*30)

""" fazendo um album de músicas """
'''def make_album(nome, titulo):
    album = {'nome': nome.title(), 'titulo': titulo.title()}

    return print(album)

#chamadas
make_album('marcos', 'soou sim')
make_album('luane', 'mais uma vez')
make_album('muri', 'tenha mais')'''

print("="*30)

#Teste 2 com parametros opcionais
def make_album(nome, titulo, faixas=0):

    if faixas:
        album = {'nome': nome.title(), 'titulo': titulo.title(), 'faixas': faixas}
    else:
        album = {'nome': nome.title(), 'titulo': titulo.title()}

    return print(album)

#chamadas
make_album('marcos', 'soou sim')
make_album('luane', 'mais uma vez')
make_album('muri', 'tenha mais', 5)

print("="*30)

#Atividade 5

'''while True:
    nome = input("Informe o nome do Album: ")
    titulo = input("Informe o titulo do album: ")
    faixas = int(input("Informe as faixas do album: ") or 0) #input valor caso não informado default 0

    make_album(nome, titulo, faixas)

    print("="*30)

    op = input("Deseja continuar? [s][n]").lower()

    if(op == 'n'):
        break'''

print("="*30)

#Atividade 6

magicos = ['paulo', 'mauro', 'lima', 'luiz', 'luana']

def show_magicians(magicos):
    for ma in magicos:
        print("Hello, {}".format(ma))

#chamadas
show_magicians(magicos)


print("="*30)

#Atividade 7
""" alterando uma lista add um elemento (o grande) ao nome do mágico na lista """
def make_great(magicos):
    for i, nome in enumerate(magicos):
        magicos[i] = "O Grande" + nome
    return magicos

'''make_great(magicos)

print(magicos)'''

print("="*30)

#Atividade 8

alter_magicos = []

alter_magicos = make_great(magicos[:])

show_magicians(magicos)
print("="*30)
show_magicians(alter_magicos)



