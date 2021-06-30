#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import openpyxl

# Carrega o arquivo Excel
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
arquivo = open('dados_planilha.txt', 'w')

# Itera por toda coluna e suas linhas, respectivamente
for coluna in sheet['A1':'C3']:
    for linha in coluna:
	    print(linha.value)
	    dados = str(linha.value)
	    arquivo.write(dados + "\n")

arquivo.close()
