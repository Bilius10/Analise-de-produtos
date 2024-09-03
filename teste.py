import time, pandas as pd
from selenium.webdriver.common.by import By
navegador = str
item = str
navegador.get(f'https://www.amazon.com.br/s?k=&__mk_pt_BR=ÅMÅŽÕÑ&crid=2VGBSGBKY6574&sprefix=wertytre%2Caps%2C256&ref=nb_sb_noss')

navegador.find_element('xpath','//*[@id="f"]').send_keys(item)
navegador.find_element('xpath','//*[@id="g"]').click()

time.sleep(1)

precos_amazon = navegador.find_elements(By.CLASS_NAME, 'a-price-whole')

nome_amazon = navegador.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")

produto = pd.DataFrame()

for x in range(0, len(precos_amazon)):
    inserir = pd.DataFrame({
        'Produto': [nome_amazon[x].text],
        'valor': [precos_amazon[x].text],
        'loja': ["Amazon"]
    })

    produto = pd.concat([inserir, produto], ignore_index=True)
