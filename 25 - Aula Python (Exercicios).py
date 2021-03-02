
# Exercicios da Aula 25
 
# Exercicio 1

'''def nome_cidade_pais(nome_cidade, nome_pais):
    retorno = f'{nome_cidade}, {nome_pais}'
    return retorno.title()'''

def nome_cidade_pais(nome_cidade, nome_pais, populacao=''):
    if populacao:
        retorno = f'{nome_cidade}, {nome_pais} - populacao {populacao}'
    else:
        retorno = f'{nome_cidade}, {nome_pais}'
    return retorno.title()

# Exercicio 2 - Continuação do 1
import unittest

class NomeCidadePaisTest(unittest.TestCase):

    def test_cidade_pais(self):
        retorno_formatado = nome_cidade_pais('brasilia', 'brasil')
        self.assertEqual(retorno_formatado, 'Brasilia, Brasil')
    
    def test_cidade_pais_populacao(self):
        retorno_formatado = nome_cidade_pais('sao luis', 'brasil', '150000')
        self.assertEqual(retorno_formatado, 'Sao Luis, Brasil - Populacao 150000')

# Chamada dos Testes
# unittest.main()

# Exercicio 3
class Employee():
 
    def __init__(self, nome, sobrenome, salario_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual

    def give_raise(self, aumento=5000):
        self.salario_anual += aumento
        return self.salario_anual

# Teste de Employee
class TesteEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('diego', 'lisboa', 20000)
    
    def test_give_default_raise(self):
        default_raise = self.employee.give_raise()
        self.assertEqual(default_raise, 25000)
    
    def test_give_custom_raise(self):
        custom_raise = self.employee.give_raise(2000)
        self.assertEqual(custom_raise, 22000)

# Teste Exercicio 3
unittest.main()