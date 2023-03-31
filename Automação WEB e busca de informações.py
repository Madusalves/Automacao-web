#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome()

# para rodar em segundo plano 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True 
navegador = webdriver.Chrome(options=chrome_options)



# passo 1 : a cotação do dolar

# entrar no google
navegador.get("https://www.google.com/")
navegador.find_element('xpath', '').send_keys("cotação dólar")

navegador.find_element('xpath', '').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','').get_attribute('data-value')

print(cotacao_dolar)


# passo 2 : a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element('xpath', '').send_keys("cotação euro")

navegador.find_element('xpath', '').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','').get_attribute('data-value')

print(cotacao_euro)


# passo 3 : a cotação do ouro 
navegador.get("")

cotacao_ouro = navegador.find_element('xpath', '').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

print(cotacao_ouro)

navegador.quit()


# In[2]:


# instalar
get_ipython().system('pip install selenium')


# In[3]:


# passo 4 : importar a base de dados e atualizar a base 
import pandas as pd

tabela = pd.read_excel(r"")
display(tabela)


# In[4]:


# passo 5 : recalcular os preços

# atualizar a cotação
# cotação dolar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# preço de compra = cotação * preço original 
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# formatar .map("R$(:2.f)".format)

display(tabela) 


# In[5]:


# passo 6 : exportar a base atuallizada 

tabela.to_excel(r"C:\Users\Maria Eduarda\Desktop\Intensivão de Python\Aula 3\Produtos Novos2.xlsx")


# In[ ]:




