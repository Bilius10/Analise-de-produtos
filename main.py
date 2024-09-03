from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=chrome_options)

item = "notebook"

navegador.get(f'https://www.mercadolivre.com.br')

navegador.find_element('xpath', '//*[@id="cb1-edit"]').send_keys(item)
navegador.find_element('xpath', '/html/body/header/div/div[2]/form/button').click()

#Necessario checar uma forma de receber os nomes e precos iguais
nome_mercadoLivre = navegador.find_elements(By.CLASS_NAME, "ui-search-item__title")

preco_mercadoLivre = navegador.find_elements(By.CSS_SELECTOR, "span[aria-label*='reais']")

avaliacao_mercadoLivre = navegador.find_elements(By.CLASS_NAME, "ui-search-reviews__rating-number")

preco_mercadoLivre_n = [preco.text.replace('\n', '') for preco in preco_mercadoLivre]
for x in preco_mercadoLivre_n:
    print(f'{x}')

print(len(preco_mercadoLivre_n))

#Rever a busca dos valores, mais valores do que produtos