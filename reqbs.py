#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import requests, bs4

req = requests.get('https://www.mercadolivre.com.br')
req.raise_for_status()
arquivo = open('ml.html', 'wb')

for chunk in req.iter_content(1000000):
	arquivo.write(chunk)

arquivo.close()

arquivo = open('ml.html', 'r')
sopa = bs4.BeautifulSoup(arquivo.read(), features="lxml")
elems = sopa.select('.ui-item__title')
elems_price = sopa.select('.price-tag-fraction')

lista = []
for i in range(5):
	print("Produto: " + elems[i].getText())
	print("Preço: " + elems_price[i].getText())

arquivo.close()

