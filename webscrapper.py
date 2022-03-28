#########################################################
# Alessandro Miranda Gonçalves                          #
# Linkedin: www.linkedin.com/alessandromirandagoncalves #
# Março/2022                                            #
#########################################################
# Programa que lê páginas HTML

from bs4 import BeautifulSoup
import requests

# Recebe o conteúdo
site = requests.get('https://www.climatempo.com.br').content

#Objeto soup recebe o conteúdo HTML
soup = BeautifulSoup(site, 'html.parser')

#Transforma o HTML em string
print(soup.prettify())

texto = soup.find("title")
print(texto.string)
#temperatura =