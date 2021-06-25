#!/usr/bin/env python3
#!-*-coding:utf-8-*-

# Importa os módulos necessários
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, bs4

# Abre o Firefox, entra no Mercado Livre e pesquisa por 'GPON' 
navegador = webdriver.Firefox()
navegador.get('https://www.mercadolivre.com.br')
texto = navegador.find_element_by_class_name('nav-search-input')
texto.send_keys('GPON')
texto.send_keys(Keys.ENTER)

# Baixa a página web e salva em um arquivo
req = requests.get('https://lista.mercadolivre.com.br/gpon#D[A:GPON]')
req.raise_for_status()
arquivo = open('ml.txt', 'wb')

for chunk in req.iter_content(1000000):
	arquivo.write(chunk)

arquivo.close()

# Faz a leitura do arquivo e filtra seu conteúdo a partir da classe dos elementos
arquivo = open('ml.txt', 'r')
sopa = bs4.BeautifulSoup(arquivo.read(), features="lxml")
elems_nome = sopa.select('.ui-search-item__title')
elems_preco = sopa.select('.price-tag-fraction')

# Retorna os nomes e preços do produto procurado
for i in range(50):
	print("Produto: " + elems_nome[i].getText())
	print("Preço: " + elems_preco[i].getText())



