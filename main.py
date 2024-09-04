from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=chrome_options)


item = "carregador"

navegador.get("https://www.buscape.com.br")

navegador.find_element(
    'xpath', '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input').send_keys(item)
navegador.find_element(
    'xpath', '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/button').click()

nome = navegador.find_elements(By.XPATH, "//*[contains(@id, 'product-card-')]")

valor =  navegador.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[7]/div/div/a/div[2]/div[2]/div[2]/p')
if len(valor) == 0:
    valor = navegador.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[6]/div/div/a/div[2]/div[2]/div[2]/p')

#Arrumar links
links = navegador.find_elements(By.TAG_NAME, "a")
link_novo = list()
for x in range(183, 207):
    href = links[x].get_attribute("href")
    link_novo.append(href)

print(len(nome))
print(len(valor))
print(len(link_novo))
produto = pd.DataFrame()

for x in range(0, len(nome)):
    inserir = pd.DataFrame({
        'nome': [nome[x].text],
        'valor': [float(valor[x].text.replace('R$ ', '').replace(',', '.'))],
        'link_novo': [link_novo[x]],
    })

    produto = pd.concat([produto, inserir], ignore_index=True)

print(produto.sort_values(by='valor'))

print(produto.dtypes)