from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import os

url = 'https://webmotors.com.br'
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(url)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/a[text()='Ver Ofertas']")))
element.click()

waittwo = WebDriverWait(driver, 5)
element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div/button[@class='tooltip_arrow_box']")))
element2.click()

inputElement = driver.find_element_by_xpath("//div/form//input[@name='anode']")
inputElement.send_keys('2003')

inputElement2 = driver.find_element_by_xpath("//div/form//input[@name='anoate']")
inputElement2.send_keys('2015')

inputElementPrecoDe = driver.find_element_by_xpath("//div/form//input[@name='precode']")
inputElementPrecoDe.send_keys(5000)

inputElementPrecoAte = driver.find_element_by_xpath("//div/form//input[@name='precoate']")
inputElementPrecoAte.send_keys(22000)

time.sleep(10)

SCROLL_PAUSE_TIME = 0.5

# Pega o tamanho da rolagem
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Desce até a parte inferior da página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Aguardar carregar
    time.sleep(SCROLL_PAUSE_TIME)

    # Calcula um novo tamanho da rolagem e compara com o ultimo tamanho
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

nomes = driver.find_elements_by_xpath("//*[@class='sc-gGBfsJ iDkBLv']")
descricoes = driver.find_elements_by_xpath("//*[@class='sc-jnlKLf elFQLq']")
precos = driver.find_elements_by_xpath("//*[@class='sc-jbKcbu esyrNH']")

nome = []
descricao = []
preco = []

for n in range(len(nomes)):
    nome.append(nomes[n].text)

for d in range(len(descricoes)):
    descricao.append(descricoes[d].text)

for p in range(len(precos)):
    preco.append(precos[p].text)


df = pd.DataFrame({'Nome': nome, 'Descricao': descricao, 'Preco': preco})
df.to_excel('webmotors.xlsx')

os.startfile('webmotors.xlsx')
