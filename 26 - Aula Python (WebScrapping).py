
# WEB SCRAPPING USANDO REQUESTS E BEAUTIFULSOAP
import requests
from bs4 import BeautifulSoup as bs

'''url = 'https://www.gruponativo.com.br'

page = requests.get(url, allow_redirects=False)

# Parseamento do HTML da Página
soup = bs(page.content, 'html.parser')
# print(page.content)

# Descobrir a ocorrências de uma tag
p = soup.find('p', class_='roxo')
# print(p)

# Visualizar o status code da requisição
print(page.status_code)

div = soup.find('div', class_='carousel-inner')

# Tag completa com conteudo
# print(div)

# Somente texto
print(div.text)

# Retornar todas as tags P
ps = soup.find_all('p')
# print(ps)'''

# Testando WebScrapping no site do Inpe de Previsão do Clima

e = input('Informe o Estado: ')
c = input('Informe o Cidade: ')

# url = "http://tempo.cptec.inpe.br"

page = requests.get('http://tempo.cptec.inpe.br/{0}/{1}'.format(e, c))

soup = bs(page.content, 'html.parser')

if(page.status_code == 200):

    cit = soup.find('label', class_='pt-1')
    cidade = cit.find('strong')
    print(f"Cidade: {cidade.text[:13]}")

    maxima = soup.find('span', class_='temp-max text-center font-dados')
    print(f"Temperatura Máxima: {maxima.text}")

    minima = soup.find('div', class_='p-1 temp-min font-dados')
    print(f"Temperatura Minima: {minima.text}")
