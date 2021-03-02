
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image

# cnpj = input('Informe o CNPJ: ')

url = 'http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/pgmei.app/Identificacao'

#Imagem a ser quebrada, neste ponto você poderia usar urlib, httplib ou curl para carregar esta imagem.
page = requests.get(url)

soup = bs(page.content, 'html.parser')

if page.status_code == 200:
    image = soup.find(id='imgCaptcha')
    #print(image['src'])
    # Pegar o CAPTCHA e desbloqueiar
    
    # Setar no Campo caracteres image o resultado do captcha
    captcha = soup.find('input', {'name': 'textoCaptcha'})
    print(captcha)