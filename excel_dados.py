#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
arquivo = open('dados_planilha.txt', 'w')
for coluna in sheet['A1':'C3']:
    for linha in coluna:
	    print(linha.value)
	    dados = str(linha.value)
	    arquivo.write(dados + "\n")

arquivo.close()
