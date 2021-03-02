#TRABALHANDO COM OO E PYTHON PT02

class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """devolve um nome descritivo do carro de forma elegante"""
        long_name = str(self.year) + " " + self.make + " " + self.model

        return long_name.title()

    def reading_odometer(self):
        """exibe uma milhagem de km do carro"""
        print("Esse carro tem {} milhas!".format(str(self.odometer_reading)))

    def update_odometer(self, mileage):
        """atualizar o valor do atributo odometer do carro"""
        """atualizar o valor somente se for maior que anterior"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Ops!! O valor tem que ser maior que o anterior!")

    def increment_odometer(self, miles):
        """incrementar um valor as milhas"""
        self.odometer_reading += miles

    def fill_gas_tanker(self):
        print("Tanque cheio de Gás!")


#INSTANCIAS

my_car = Car('audi', 'a4', 2016)

print(my_car.get_descriptive_name())

#ALTERANDO DIRETAMENTE O VALOR DE ATRIBUTO DA CLASSE
#(OBS. SEGUNDO O PILAR DE ENCAPSULAMENTO ISSO NÃO É RECOMENDADO)
my_car.odometer_reading = 23

#Modificando o valor de um atributo com um método
#(Obs. Usando um metodo set forma mais adequada, obedecendo o
#encapsulamento)
my_car.update_odometer(100)

#Incrementar o valor de odometer_milhas
my_car.increment_odometer(300)

my_car.reading_odometer()


print("="*30)


#NOVO TÓPICO HERANÇA

class Batery():
    """Modelando a bateria de um carro eletrico"""

    def __init__(self, batery_size = 70):
        """inicializa os atributos da bateria"""
        self.batery_size = batery_size

    def describe_battery(self):  # exibe uma frase que descrevea capacidade da bateria
        print("Esse carro tem {} -kwh de energia na bateria!".format(self.batery_size))

    def set_describe_battery(self, batery):
        self.batery_size = batery

    def get_range(self):
        """"Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria"""
        range = 0
        if self.batery_size == 70: range = 240
        elif self.batery_size == 85: range = 270

        message = "Esse carro percorre aproximadamente "+ str(range)
        message += " km por carga!"

        print(message)

    def upgrade_batery(self):
        if self.batery_size != 85:
            self.batery_size = 85


class ElectricCar(Car):#Em python não existe (extends) (herdar passando a classe nos () da classe
    """representa aspectos espécificos de carros"""

    def __init__(self, make, model, year):
        """inicializa atributos da classe pai"""
        super().__init__(make, model, year)
        #super() chamar o construtor da classe pai (com seus atributos)
        #referência a classe Car() pai

       # self.batery_size = 70
        self.batery = Batery()


    #def describe_battery(self): #exibe uma frase que descrevea capacidade da bateria
     #   print("Esse carro tem {} -kwh de energia na bateria!".format(self.batery_size))

    #def set_describe_battery(self, batery):
     #   self.batery_size = batery

    def fill_gas_tanker(self):
        print("Esse carro não precisa de um tank de Gás!")


#INSTÂNCIA
my_tesla = ElectricCar("tesla", "model_s", 2016)

print(my_tesla.get_descriptive_name())

my_tesla.batery.set_describe_battery(85)
#my_tesla.describe_battery()

my_tesla.fill_gas_tanker()

my_tesla.batery.describe_battery()

my_tesla.batery.get_range()

#ATIVIDADE 3
my_el = ElectricCar("car", "2011-1", 2011)

my_el.batery.set_describe_battery(12)

my_el.batery.get_range()

my_el.batery.upgrade_batery()

my_el.batery.get_range()



