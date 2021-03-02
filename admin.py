
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
      #      print("Poderes