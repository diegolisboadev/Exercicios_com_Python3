#Utilizando o Packing para para chamar a função de
#forma mais elegante

def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {'active': False,
          'admin': True
          }

new_user(**config)#* -- Representa o Packing - ** dicionario
