#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import requests, bs4

req = requests.get("https://www.mercadolivre.com.br/")
req.raise_for_status()
arquivo = open("mercado_livre.txt", "w")
arquivo.write(req.text)
arquivo.close()

def extrai_dados():
	sopa = open('mercado_livre.txt')
	soup = bs4.BeautifulSoup(sopa)
	filtra_nome = soup.select('.ui-item__title')
	filtra_preco = soup.select('.price-tag-fraction')
	for i in range(5):
		print("Produto: " + str(filtra_nome[i].getText()) + " Preço: " + str(filtra_preco[i].getText()))

extrai_dados()




