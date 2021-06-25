#!/usr/bin/env python3
#!-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, bs4

navegador = webdriver.Firefox()
navegador.get('https://www.mercadolivre.com.br')
texto = navegador.find_element_by_class_name('nav-search-input')
texto.send_keys('GPON')
texto.send_keys(Keys.ENTER)

req = requests.get('https://lista.mercadolivre.com.br/gpon#D[A:GPON]')
req.raise_for_status()
arquivo = open('ml.txt', 'wb')

for chunk in req.iter_content(1000000):
	arquivo.write(chunk)

arquivo.close()

arquivo = open('ml.txt', 'r')
sopa = bs4.BeautifulSoup(arquivo.read(), features="lxml")
elems_nome = sopa.select('.ui-search-item__title')
elems_preco = sopa.select('.price-tag-fraction')

for i in range(50):
	print("Produto: " + elems_nome[i].getText())
	print("Preço: " + elems_preco[i].getText())



