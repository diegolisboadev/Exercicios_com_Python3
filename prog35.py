# ATIVIDADE 2 DE CLASSES  PYTHON

from prog34 import Restaurant, User


#ATIVIDADE 1
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        # lista de sabores de sorvete
        self.flavors = ['morango', 'chocolate', 'uva', 'granulado', 'goma grolada']

    def sabores_sorvete(self):
        for fl in self.flavors:
            print("Sabor {} contido!!".format(fl))


#INSTANCIA

ice = IceCreamStand('sousa sorvetes', 'Brazil')

ice.sabores_sorvete()


print("="*30)

#ATIVIDADE 3

class Privileges():

    def __init__(self):

        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
       for adm in self.privileges:
          print("Poderes do Administrador {}".format(adm))


#ATIVIDADE 2

class Admin(User):

    def __init__(self, first_name, last_name, cpf, idade):
        super().__init__(first_name, last_name, cpf, idade)

        #self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()

    #def show_privileges(self):
     #   for adm in self.privileges:
      #      print("Poderes do Administrador {}".format(adm))


#INSTANCIA

admin = Admin('Diego', 'Pires', 123123123, 25)

#admin.show_privileges()

print("="*30)

#INSTANCIA ADMIN 2

admin2 = Admin("Paulo", 'Pedro', 21231231, 21)

admin2.privileges.show_privileges()


print("="*30)

#ATIVIDADE 4

