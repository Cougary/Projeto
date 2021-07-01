#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2

# Define o arquivo que será lido
arquivo = input("Digite o arquivo em PDF a ser lido: ")
pdf = open(arquivo, 'rb')
pdfler = PyPDF2.PdfFileReader(pdf)

# Itera sobre todas as páginas do arquivo em PDF e mostra seu conteúdo
for pagina in range(pdfler.numPages):
	paginaobj = pdfler.getPage(pagina)
	print(paginaobj.extractText())
