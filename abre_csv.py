#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import csv

texto = input("Digite o arquivo csv que deseja abrir: ")
arquivo = open(texto)
leitor = csv.reader(arquivo)

for linha in leitor:
    print("Linha # " + str(leitor.line_num) + " " + str(linha))
