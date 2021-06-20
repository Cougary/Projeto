#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import pyperclip
import os

# Transferindo do clipboard o que foi copiado para um arquivo

def copia():	
	texto = input("Insira o texto copiado: ")
	copia  = pyperclip.copy(texto)
	cola = pyperclip.paste(copia)
	arquivo = open("copia.txt", "w")
	arquivo.write(cola + "\n")
	arquivo.close()
	print("Cópia inserida no arquivo.")

copia()
