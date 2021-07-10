import requests
import random

class Chatbot:

    nome_chatbot = 'DuChat'

    def __init__(self) -> None:
        pass

    def sequencia_fibonacci(self):
        n = int(input("Que termo deseja encontrar: "))
        ultimo=1
        penultimo=1

        if (n==1) or (n==2):
            print("1")
        else:
            for count in range(2,n):
                termo = ultimo + penultimo
                penultimo = ultimo
                ultimo = termo
                count += 1
                print(termo, end=' -> ')

    def descubra_seu_signo(self, dia, mes):
        if mes == 'dezembro':
            astro_sign = 'Sagittarius' if (dia < 22) else 'capricorn'
        elif mes == 'janeiro':
            astro_sign = 'Capricorn' if (dia < 20) else 'aquarius'
        elif mes == 'fevereiro':
            astro_sign = 'Aquarius' if (dia < 19) else 'pisces'
        elif mes == 'março':
            astro_sign = 'Pisces' if (dia < 21) else 'aries'
        elif mes == 'abril':
            astro_sign = 'Aries' if (dia < 20) else 'taurus'
        elif mes == 'maio':
            astro_sign = 'Taurus' if (dia < 21) else 'gemini'
        elif mes == 'junho':
            astro_sign = 'Gemini' if (dia < 21) else 'cancer'
        elif mes == 'julho':
            astro_sign = 'Cancer' if (dia < 23) else 'leo'
        elif mes == 'agosto':
            astro_sign = 'Leo' if (dia < 23) else 'virgo'
        elif mes == 'setembro':
            astro_sign = 'Virgo' if (dia < 23) else 'libra'
        elif mes == 'outubro':
            astro_sign = 'Libra' if (dia < 23) else 'scorpio'
        elif mes == 'novembro':
            astro_sign = 'scorpio' if (dia < 22) else 'sagittarius'
        print(astro_sign)

    def piada(self):
        piada = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
        print(piada.json()['joke'])

    def charada(self):
        charadas = {'pergunta': 'Sem sair do seu cantinho, é capaz de viajar ao redor do mundo.',
                    'resposta': 'selo', 
                    'pergunta': 'É feito de água, mas se for colocado dentro da água morrerá.',
                    'resposta': 'gelo'
                }
        charada = input(f'O que é o que é? {random.choices(list(charadas.keys()))}')
        return charadas['resposta'] == charada
        
    def get_nome_chatbot(self):
        return self.nome_chatbot

def main():
    print('-='*20)
    print('\n 1 = SEQUÊNCIA DE FIBONNACCI \n 2 = DESCUBRA SEU SIGNO \n 3 = DESCUBRA MEU NOME \n 4 = PIADA \n 5 = CHARADA')
    opcao = int(input('Como posso lhe ajudar? '))
    print('-='*20)

    chatbot = Chatbot()
    
    if opcao == 1:
        print('Sequência de Fibonnaci')
        print(chatbot.sequencia_fibonacci())
    elif opcao == 2:
        dia = int(input('Informe seu dia de nascimento: '))
        mes = input('Informe o seu mês de nascimento: ')
        chatbot.descubra_seu_signo(dia, mes)
    elif opcao == 3:
        print(f'Olá me chamo {chatbot.get_nome_chatbot()}')
    elif opcao == 4:
        chatbot.piada()
    elif opcao == 5:
        chatbot.charada()
    else:
        print('Valor Inválido!')
if __name__ == "__main__":
    main()
