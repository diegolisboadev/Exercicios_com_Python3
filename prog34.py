
#ATIVIDADE 2 DE CLASSES  PYTHON
from datetime import date, datetime
from time import sleep

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print("Nome Restaurante: {}".format(self.restaurant_name))
        print("\nCusisine: {}".format(self.cuisine_type))

    def open_restaurante(self):
        print("O Restaurante está aberto!!")

    def set_number_served(self, num):
        self.number_served = num
        return self.number_served

    def increment_number_served(self, num):
        self.number_served += num
        return self.number_served

#INSTANCIAS

restaurant = Restaurant('plol', 'brazil')

restaurant.describe_restaurant()

data_format = date.today().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M:%S")

teste = restaurant.set_number_served(50)
print("Hoje {} às {} foram atendidos {} ".format(data_format, hora, teste))

#LOOP COM sleep() para mostrar barra de carregamento
for t in range(10):
    sleep(t)
    print(end="...")

teste2 = restaurant.increment_number_served(100)
print("\nE agora {} ás {} foram atendidos {}".format(data_format, hora, teste2))

print("="*30)

class User():

    def __init__(self, first_name, last_name, cpf, idade):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.idade = idade
        self.login_attempts = 0

    def describe_user(self):
        print("Primeiro Nome: {}"
              "\nÚltimo Nome: {}"
              "\nCPF: {}"
              "\nIDADE: {}".format(self.first_name, self.last_name, self.cpf, self.idade))

    def greet_user(self):
        print("Bem Vindo: {}"
              "\nSeu CPF: {}"
              "\nSua IDADE: {}".format((self.first_name + " " + self.last_name), self.cpf, self.idade))

    def increments_login(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login(self):
        self.login_attempts = 0
        return self.login_attempts


#INSTÂNCIAS

user = User('diego', 'pires', 12345678900, '35')

inc = user.increments_login()
print(inc)
inc2 = user.increments_login()
print(inc2)
inc3 = user.increments_login()
print(inc3)
inc4 = user.increments_login()
print(inc4)

print("Login: {}".format(user.login_attempts))

rese = user.reset_login()

print("Login: {}".format(user.login_attempts))