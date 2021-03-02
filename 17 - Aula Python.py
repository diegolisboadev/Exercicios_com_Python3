#Funções

"""Mostrar uma mensagem de boas vindas ao usuário"""
def prazer(username):
    print("Prazer {}!!".format(username))


prazer('Diego')


#Lição 2
#Argumentos Posicionais -> ordem de passagem argumento -> parametro deve
#está correta

def animal_desc(nome_animal, tipo_animal="peixe"):
    print("Eu tenho um(a) {}".format(tipo_animal))
    print("Meu {} tem o nome de {}".format(tipo_animal, nome_animal))

animal_desc("cao", "pig")

print("="*30)

animal_desc("gato", "cat")

print("="*30)

#Lição 3
#Argumentos Posicionais
#Não tem preocupação com a ordem -> o parametro já recebe o
#seu argumento previamente na chamada da função

animal_desc(nome_animal="Figo", tipo_animal="aranha")

print("="*30)

#Lição 4
#Parametro default
#Parametro com valor predefinido na criação da
#função

animal_desc("pulinho")

#Lição 5

#animal_desc() #erro traceback (faltou um argumento posicional na função)

print("="*30)

#Lição 6

def nomeFormatado(nome, sobrenome):
    print("Nome formatado: {} {}".format(nome.capitalize(), sobrenome.capitalize()))


nomeFormatado("diego", "pires")

#Lição 7

"""nome completo formatado"""
def nomeFormatadoCompleto(nome, meio, sobrenome):
    nome_completo = "Nome formatado: {} {} {}".format(nome.capitalize(), meio.capitalize(), sobrenome.capitalize())
    return nome_completo


nome = nomeFormatadoCompleto("diego", "lisboa", "pires")
print(nome)

print("="*30)

"""nome completo formatado com parametro opcional"""
def nomeFormatadoCompleto(nome, ultimo_nome, meio=""):
    if meio:
        nome_completo = "Nome formatado: {} {} {}".format(nome.capitalize(), meio.capitalize(), ultimo_nome.capitalize())
    else:
        nome_completo = "Nome formatado: {} {}".format(nome.capitalize(), ultimo_nome.capitalize())

    return nome_completo


nome = nomeFormatadoCompleto("diego", "pires", "lisboa")
print(nome)

print("="*30)

#Lição 7

""" devolve um dicionário com informações sobre uma pessoa """
def build_person(first_name, last_name):
    pessoa = {'first': first_name, 'last': last_name}
    return pessoa

pessoa = ("luma", "silva")

print(pessoa)

print("="*30)

""" devolve um dicionário com informações sobre uma pessoa """
def build_person_complete(first_name, last_name, age=""):
    pessoa = {'first': first_name, 'last': last_name}
    if age:
        pessoa[age] = age

    return pessoa

pessoa = ("luma", "silva", 30)

print(pessoa)

print("="*30)

#PASSANDO UMA LISTA PARA UMA FUNÇÃO

def prazer(usuarios):
    for user in usuarios:
        print("Nice to meet you {}".format(user.title()))

#chamada
pessoas = ['diego', 'luane', 'mila']

prazer(pessoas)

print("="*30)

#Modificando listas nas funções em python

unprinted_design = ['iphone_case', 'robot_case', 'dodecahedron']
copy_unprinted_designs = unprinted_design[:] #caso seja melhor utilizar(preservar a lista original)
completed_models = []

'''while unprinted_design:
    current_designs = unprinted_design.pop()
    print("Imprimindo Model: {}".format(current_designs))

    completed_models.append(current_designs)

print("\n O seguinte modelo foi impresso: ")
for completed in completed_models:
        print(completed)'''

#Modificando listas usando funções com python

def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_designs = unprinted_design.pop()
        print("Imprimindo Model: {}".format(current_designs))

        completed_models.append(current_designs)

def show_completed_models(completed_models):
    print("\n O seguinte modelo foi impresso: ")
    for completed in completed_models:
        print(completed)

#chamadas
print_models(unprinted_design, completed_models)
show_completed_models(completed_models)

print("="*30)

#NÚMERO ARBITRÁRIO DE ARGUMENTOS
#passar uma quantidade minima ou máxima de parametros
# O asterisco no nome do parâmetro *toppings diz a Python para criar
# uma tupla vazia chamada toppings e reunir os valores recebidos na tupla.

def make_pizza(*toppings):
    for top in toppings:
        print("Pedido de Pizza do tipo: {}".format(top))

#chamada
make_pizza('peperroni')
make_pizza('mussarela', 'calabresa', 'portuguesa')

#ARGUMENTOS NOMEADOS ARBITRÁRIOS
## (**) caso use parametros arbitrários nomeados na função
#Os asteriscos duplos antes do parâmetro **user_info fazem Python criar um dicionário vazio chamado
#user_info e colocar quaisquer pares nome-valor recebidos nesse dicionário.
def build_profile(first, last, **user_info):
    profile = {}

    profile['fisrt_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('diego', 'pires', location='brasil', field='fisica')

print(user_profile)




