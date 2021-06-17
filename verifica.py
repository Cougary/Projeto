#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import os
import sys

# Lista diretório
print("Digite 'EXIT' caso queira sair do programa.")
while True:
	try:
		dirc = input("Digite o diretório que deseja listar: ")
		if (dirc == "EXIT"):
			break
			sys.exit()
		diretorio = os.listdir(dirc)

		for arquivo in diretorio:
			print(arquivo)

	except Exception as erro:
		print("Erro: " + str(erro))
