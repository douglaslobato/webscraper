from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv

html = urlopen("https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-2020/agenda-tributaria-janeiro-2020/dia-06-01-2020")
bs = BeautifulSoup(html, 'html.parser')

linhas = bs.find_all('tr', {'class':'even'})

codigo = []
descricao = []
periodo = []

for i in linhas:
    filhas = i.findChildren("td")
    codigo.append(filhas[0].text)
    descricao.append(filhas[1].text)
    periodo.append(filhas[2].text)

df = pd.DataFrame({'Codigo': codigo, 'Descricao': descricao, 'Periodo': periodo})

df.to_excel('teste.xlsx')