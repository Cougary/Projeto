#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import openpyxl, sys

if len(sys.argv) < 3:
	print("Usage: python3 blank.py <linha> <arquivo>")
	sys.exit()

planilha = sys.argv[2]
linha = sys.argv[1]
wb = openpyxl.load_workbook(planilha)
sheet = wb['Sheet']
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in alfabeto:
    sheet[i + str(linha)].value = ""
	
wb.save('nova_planilha.xlsx')




