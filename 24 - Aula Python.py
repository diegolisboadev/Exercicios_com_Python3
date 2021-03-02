
#AULA PYTHON

import json

numbers = [2,3,5,7,11,13]

filename = 'text_files/numbers.json'

try:
    with open(filename, 'w') as file:
        json.dump(numbers, file)
except FileNotFoundError:
    print("Arquivo {} não pode ser criado".format(filename))

#LENDO INFO

try:
    with open(filename) as fil_c:
        numbers = json.load(fil_c)
        print(numbers)
except FileNotFoundError:
    print("Erro ao ler o arquivo {}".format(filename))


#SALVANDO E LEMBRANDO NOME USUÁRIO

'''username = input("Qual o seu nome? ")
filename = 'text_files/username.json'

try:
    with open(filename, 'w') as file_u:
        json.dump(username, file_u)
except FileNotFoundError:
    print("Não foi possivel lembrar seu nome {}".format(username.title()))

#LENDO O NOME USER

try:
    with open(filename) as file_r:
        nome = json.load(file_r)
        print("Seja bem Vindo {}".format(nome))
except FileNotFoundError:
    print("Erro na leitura do nome.")'''

#EXEMPLO 3

'''filename = "text_files/username.json"

try:
    with open(filename) as f_read:
        username = json.load(f_read)
        print("Bem vindo {}".format(username))
except FileNotFoundError:
    username = input("Informe seu Nome: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("Nome salvo, para relembrar {}".format(username))'''

#EXEMPLO 4

'''def greet_user():
    """sauda usuario pelo nome"""
    filename = "text_files/username.json"

    try:
        with open(filename) as f_read:
            username = json.load(f_read)
            print("Bem vindo {}".format(username))
    except FileNotFoundError:
        username = input("Informe seu Nome: ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("Nome salvo, para relembrar {}".format(username))'''

def get_stored_username():
    """Obtém o nome do usuário já armazenado se
estiver disponível"""
    filename = 'text_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

'''def greet_user():
    """sauda usuario pelo nome"""
    filename = "text_files/username.json"

    username = get_stored_username()
    if username:
        print("Bem vindo {}".format(username))
    else:
        username = input("Informe seu nome: ")

        with open(filename, 'w') as fo:
            json.dump(username, fo)
            print("Nome salvo, para relembrar {}".format(username))'''

def get_new_username():
    """pede um novo nome de usuário"""

    username = input("Qual e o seu nome? ")

    filename = 'username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    """Saúda o usuário pelo nome. """

    username = get_stored_username()

    if username:
        print("bem vindo de volta, " + username + "!")
    else:
        username = get_new_username()
        print("Nó lembraremos seu nome, " + username + "!")

greet_user()
