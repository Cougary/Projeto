#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import zipfile

arquivo_zip =  input("Digite o arquivo zipado: ")
zipado = zipfile.ZipFile(arquivo_zip)
lista = zipado.namelist()

print("Arquivos e diretórios presentes no arquivo zipado: ")

for arquivo in lista:
	info = zipado.getinfo(arquivo)
	print("Nome: " + arquivo + " Tamanho: " + str(info.file_size) + " bytes")

