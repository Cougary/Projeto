#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import csv, openpyxl

arquivo = input("Digite o arquivo CSV: ")
exemplo = open(arquivo)
exemploLer = csv.reader(exemplo)
lista = []
for linha in exemploLer:
    print(linha)
    lista.append(linha)

print(lista)

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = str(lista)
wb.save('copia_csv.xlsx')
