# Web Scraping de pesquisa de climas nas cidades e estados do Brasil com Python usando BeautifulSoup e Selenium.

# Importações necessárias
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

# Diretório padrão (onde salvará os registros)
os.chdir("C:/Users/rahsouza/Desktop/Scrap")

# Cidades, Estado e País para pesquisa:
Cidades = ['Bauru, São Paulo, Brasil', 'São Paulo, São Paulo, Brasil', 'Rio de Janeiro, Rio de Janeiro, Brasil']

# carregamento do driver e inclusão da url
browser = webdriver.Chrome(executable_path="C:/Users/rahsouza/Desktop/Scrap/chromedriver")
url = 'https://weather.com/pt-BR/clima/10dias/l/BRMG0645:1:BR';
browser.get(url)

# laço de repetição para as cidades
for cidade in Cidades:
    
    #Criação de arquivo txt com as consultas
    txtName = cidade + ".txt";
    f = open(txtName,"w+")
    
    #Seleção do campo de input
    print("Cidade, Estado e País: ", cidade)
    fieldSearch = browser.find_element_by_css_selector(".theme__inputElement__4bZUj.input__inputElement__1GjGE")
    
    #Timer de espera de carregamento da pagina
    time.sleep(3);
    
    #Inclusão da Cidade, Estado e País na pesquisa
    fieldSearch.send_keys(cidade)
    
    #Timer de espera de carregamento da pagina
    time.sleep(3)
    
    fieldClicked = browser.find_element_by_css_selector(".styles__item__3sdr8.styles__selected__SEH0e")
    
    #Timer de espera de carregamento da pagina
    time.sleep(3)
    
    #Click no campo pesquisado
    fieldClicked.click()
    
    #Utilização do Beautifulsoup pra captura de informações
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    #Criação de tabela
    table = soup.find('table', attrs={'class':'twc-table'})
    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    #Escrita das linhas lidas
    for row in rows:
     cols = row.find_all('td')
     cols = [ele.text.strip() for ele in cols]
     data.append([ele for ele in cols if ele])
     info = [ele for ele in cols if ele]
     post = {
     "Dia" : info[0],
     "Descrição" : info[1],
     "Max/Min" : info[2],
     "Precipitação" : info[3],
     "Vento" : info[4],
     "Umidade" : info[5]
     }
     txtLine = "Dia: " + info[0] + " Descrição: " + info[1] + " Max/Min: " + info[2] + " Precipitação: " + info[3] + " Vento: " + info[4] + " Umidade: " + info[5]
     txtLine += "\n"
     f.write(txtLine)
     f.write("---------------\n")
     print(post)
    
     print("---------------")

# Fechando browser
browser.close()

