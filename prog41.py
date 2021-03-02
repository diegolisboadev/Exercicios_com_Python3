
#ATIVIDADE 1

import json
'''
def pegarNumFavorito(filename):

    num = int(input("Informe seu número favorito: "))

    try:
        with open(filename, 'w') as file_w:
            json.dump(num, file_w)
    except FileNotFoundError:
        print("Erro ao abrir o arquivo.")

def listarNumFavorito(filename):
    try:
        with open(filename) as file_r:
            contents = json.load(file_r)

    except FileNotFoundError:
        return None
    else:
        return contents


#EXECUTANDO ATIVIDADE

filename = "text_files/num_favorito.json"

pegarNumFavorito(filename)

num = listarNumFavorito(filename)
print("Eu sei qual é o seu número favorito! É " + str(num))'''

#ATIVIDADE 2
'''
def pegarNumFavorito(filename):

    try:
        with open(filename) as file_w:

            contents = json.load(file_w)
            print("Eu sei qual é o seu número favorito! É {}".format(contents))

    except FileNotFoundError:

        num = int(input("Informe seu número favorito: "))

        with open(filename, 'w') as file_r:
            json.dump(num, file_r)
            print("Número {} armazenado".format(num))


#EXECUTANDO ATIVIDADE

filename = "text_files/num_favorito.json"

pegarNumFavorito(filename)'''

#ATIVIDADE 3

def get_stored_username():
    """"Obtém o nome do usuário já armazenado se estiver disponível"""

    filename = 'text_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """pede um novo nome de usuário"""

    username = input("Qual e o seu nome? ")

    filename = 'text_files/username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    """Saúda o usuário pelo nome. """

    username = get_stored_username()

    if username:

        print("Olá {}".format(username))

        username_verif = input("Seu nome está correto? [S/N]").upper()

        if username_verif == 'S':
            print("bem vindo de volta, " + username + "!")
        else:
            get_new_username()
    else:
        username = get_new_username()
        print("Nó lembraremos seu nome, " + username + "!")

greet_user()