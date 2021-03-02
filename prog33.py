#ATIVIDADE DE CLASSES  PYTHON

from sys import exit

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Nome Restaurante: {}".format(self.restaurant_name))
        print("\nCusisine: {}".format(self.cuisine_type))

    def open_restaurante(self):
        print("O Restaurante está aberto!!")



#INSTANCIAS DE RESTAURANTE
restaurant = Restaurant("Palotine", 'mais umas vez!')

print(restaurant.restaurant_name)
print("="*20)
print(restaurant.cuisine_type)

print("="*30)

restaurant.describe_restaurant()
restaurant.open_restaurante()


print("="*50)

restaurant2 = Restaurant("novo_mirim", "italiana")
restaurant3 = Restaurant("tropeiro", 'rio grandense')
restaurant4 = Restaurant("mara_come", 'maranhense')

restaurant2.describe_restaurant()
print("\n")
restaurant3.describe_restaurant()
print("\n")
restaurant4.describe_restaurant()


print("="*50)


class User():

    def __init__(self, first_name, last_name, cpf, idade):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.idade = idade

    def describe_user(self):
        print("Primeiro Nome: {}"
              "\nÚltimo Nome: {}"
              "\nCPF: {}"
              "\nIDADE: {}".format(self.first_name, self.last_name, self.cpf, self.idade))

    def greet_user(self):
        print("Bem Vindo: {}"
              "\nSeu CPF: {}"
              "\nSua IDADE: {}".format((self.first_name + " " + self.last_name), self.cpf, self.idade))


#INSTÂNCIAS

user = User("Diego", 'Pires', 12345678900, 23)
user2 = User("Mariana", "Lisboa", 12345678900, 30)

user.describe_user()
user.greet_user()

print("="*30)

user2.describe_user()
user2.greet_user()