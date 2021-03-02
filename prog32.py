
#ATIVIDADE 1 MÓDULOS IMPORT

import modulo_printing as mp
#import modulo
#from modulo import imprimir_nome
from modulo import imprimir_nome as im
#import modulo as m
#from modulo import *

unprinted_design = ['iphone_case', 'robot_case', 'dodecahedron']
copy_unprinted_designs = unprinted_design[:] #caso seja melhor utilizar(preservar a lista original)
completed_models = []

mp.print_models(unprinted_design, completed_models)
mp.show_completed_models(completed_models)

#ATIVIDADE 2

im("diego")

#ATIVIDADE 3
print("ok")