#Testando a função com packing usando parametros nomeados
#Nomeando com a utilização de dicionários

def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {'active': False,
          'admin': True
          }

new_user(config.get('active'), config.get('admin'))
