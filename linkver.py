#!/usr/bin/env python3
#!-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, bs4

# Acessa o site desejado
url = input("Digite o site que deseja acessar: ")
browser = webdriver.Firefox()
browser.get(url)

req = requests.get(url)
req.raise_for_status()

# Salva o site baixado em um arquivo HTML
arquivo = open('link.html', 'wb')

for chunk in req.iter_content(100000):
	arquivo.write(chunk)

arquivo.close()

# Lê o arquivo HTML e retorna todos os links da página
arquivo = open('link.html', 'rb')
sopa = bs4.BeautifulSoup(arquivo.read(), features="lxml")
elem = sopa.select('a')

for i in range(len(elem)):
	print("Link: " + elem[i].getText())
