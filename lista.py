#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import os 

# Listando um diretório e lendo um determinado arquivo

caminho = input("Digite o diretório que quer listar: ")
diretorio = os.listdir(caminho)

for arquivo in diretorio:
	print(arquivo)

texto = input("Digite o arquivo do diretório listado que deseja ler: ")
arquivo = open(texto, "r")

for linha in arquivo:
	print(linha)
