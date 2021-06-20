#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import shutil
import os

diretorio = input("Digite o diretório que deseja fazer o backup: ")
destino = input("Digite o destino do backup: ")
shutil.copytree(diretorio, destino)

print("Backup do diretório: ")

for arquivo in os.listdir(diretorio):
	print(arquivo)
