
import unittest
from sessao_teste_py.names_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """testes para name function"""

    def test_first_last_name(self):
        """nomes como Janis Joplin funcionam"""
        formated_name = get_formated_name("janis", "oplin")
        self.assertEqual(formated_name, 'Janis Joplin')


test = NamesTestCase()
test.test_first_last_name()

unittest.main()