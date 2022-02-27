from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import requests

from src.fun import decimal, integer

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

html = requests.get('https://www.fundamentus.com.br/detalhes.php?papel=ABEV3', headers = agent).text

bs = BeautifulSoup(html, 'lxml')

tables = bs.find_all('table')

# Transforming text into number functions

fundamentus = {
    'codigo':tables[0].find_all('td')[1].text,
    'setor':tables[0].find_all('td')[13].text,
    'subsetor':tables[0].find_all('td')[17].text,
    'preco':decimal(tables[0].find_all('td')[3].text),
    'volume':integer(tables[0].find_all('td')[19].text)
}

df = pd.DataFrame([fundamentus])

# db

conn = sqlite3.connect('data/stocks.db')

df.to_sql('tb_fundamentus', index = False, if_exists = 'replace', con = conn)

conn.close()