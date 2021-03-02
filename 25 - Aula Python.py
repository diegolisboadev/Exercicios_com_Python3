
#TESTE DE CÓDIGO PYTHON

'''def get_formated_name(first, last):
    """formatar uma saída para nome e sobrenome"""
    nome_completo = f'{first} {last}'
    return nome_completo.title()'''

def get_formated_name(first, middle, last=''):
    """formatar uma saída para nome e sobrenome"""
    if last:
        nome_completo = f'{first} {middle} {last}'
    else:
        nome_completo = f'{first} {middle}'
    return nome_completo.title()

# Saída
'''print('Informe q para finalizar o programa.')
while True:
    first = input('Informe seu Primeiro Nome: ') 
    if first.lower() == 'q': break
    last = input('Informe seu Sobrenome: ') 
    if last.lower() == 'q': break
    nome_formatado = get_formated_name(first, last)
    print(f'Nome Formatado {nome_formatado}.')'''

import unittest

class NameTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        """ Testa nome e sobrenome """
        nome_formatado = get_formated_name('diego', 'lisboa')
        self.assertEqual(nome_formatado, 'Diego Lisboa')

    def test_first_middle_last_name(self):
        """ Nomes como Diego Lisboa Pires funcionam """
        nome_formatado = get_formated_name('diego', 'lisboa', 'pires')
        self.assertEqual(nome_formatado, 'Diego Lisboa Pires')



# Executar o Teste Unitário
# unittest.main()

# Testando Classes
class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa. """

    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as respostas.""" 
        self.question = self.responses = []
        
    def show_question(self):
        """Mostra a pergunta da pesquisa.""" 
        print(question)
    
    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa.""" 
        self.responses.append(new_response)
    
    def show_results(self):
        """Mostra todas as respostas dadas."""
        print('Respostas Informadas: ')
        for response in self.responses:
            print(f'- {response}')

# Declarando e Instanciando a Classe AnonymousSurvey

# Define uma pergunta e cria uma pesquisa 
question = 'Qual linguagem você aprendeu a falar primeiro?'
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta 
my_survey.show_question()
print('Informe (q) para parar o programa!')
while True:
    response = input('Linguagem: ')
    if response.lower() == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa 
print('Obrigado por suas respostas!!')
my_survey.show_results()

# Testando AnonymousSurvey Class
class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def setUp(self):
        """ Cria uma pesquisa e um conjunto de respostas que poderão ser usados
        em todos os métodos de teste. (Criar um objeto da Classe a ser usado em 
        todo o Código """
        question = "Qual linguagem você aprendeu a falar primeiro?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Inglês', 'Português', 'Espanhol',]
 

    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self): 
        """Testa se três respostas individuais são armazenadas de forma apropriada.""" 

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses) 


# Testando Comportamentos da Classe
unittest.main()