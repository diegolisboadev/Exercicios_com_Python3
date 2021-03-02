#TRABALHANDO COM OO E PYTHON

class Dog():

    """MODELANDO UM CLASSE"""

    def __init__(self, name, age):

        self.name = name
        self.age = age

    """cachorro sentando"""
    def sit(self):
        print("{} está sentando.".format(self.name.title()))

    """simular o cachorro rolando"""
    def rool_over(self):
        print("{} rolando.".format(self.name.title()))



#INSTANCIANDO

my_dog = Dog('thor', 10)

print(my_dog.name)
print(my_dog.age)

my_dog.sit()
my_dog.rool_over()

print("="*30)

#SEGUNDA INSTÂNCIA DE CACHORRO

your_dog = Dog('dog', 20)

print(your_dog.name)
print(your_dog.age)

your_dog.sit()
your_dog.rool_over()