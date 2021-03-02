
#ATIVIDADE 1

from collections import OrderedDict
from random import randint

favorite_laguagens = OrderedDict()

favorite_laguagens['jen'] = 'python'
favorite_laguagens['sarah'] = 'c'
favorite_laguagens['sarah'] = 'ruby'
favorite_laguagens['eadwar'] = 'ruby'
favorite_laguagens['phil'] = 'python'

for name, languages in favorite_laguagens.items():
    print("{}'s favorita linguagem {}".format(name.title(), languages.title()))


#ATIVIDADE 2

class Die():

    def __init__(self, sides = 6):

        self.sides = sides

    def roll_die(self):
        print("{} lados".format(randint(1, self.sides)))


#INSTANCIANDO

dado = Die()

dado.roll_die()

dados = Die(10)

dados.roll_die()

d = Die(20)

d.roll_die()


#ATIVIDADE 3
