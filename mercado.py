#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import requests, bs4

# Baixa a página web e salva seu conteúdo no arquivo 'mercado_livre.txt'
req = requests.get("https://www.mercadolivre.com.br/")
req.raise_for_status()
arquivo = open("mercado_livre.txt", "w")
arquivo.write(req.text)
arquivo.close()

# Função que extrai e filtra os dados do arquivo baixados para retornar os nomes e preços dos produtos encontrados
def extrai_dados():
	sopa = open('mercado_livre.txt')
	soup = bs4.BeautifulSoup(sopa, features="lxml")
	filtra_nome = soup.select('.ui-item__title')
	filtra_preco = soup.select('.price-tag-fraction')
	for i in range(5):
		print("Produto: " + str(filtra_nome[i].getText()) + " Preço: " + str(filtra_preco[i].getText()))

# Chama a função anteriormente definida
extrai_dados()




