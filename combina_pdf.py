#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2

# Define os arquivos que serão combinados
arquivo1 = input("Digite o arquivo com o path absoluto: ")
arquivo2 = input("Digite outro arquivo com o path absoluto: ")
pdf1 = open(arquivo1, 'rb')
pdf2 = open(arquivo2, 'rb')
pdf1ler = PyPDF2.PdfFileReader(pdf1)
pdf2ler = PyPDF2.PdfFileReader(pdf2)
pdfescreve = PyPDF2.PdfFileWriter()

# Itera sobre todas as páginas do arquivo em PDF
for pagina in range(pdf1ler.numPages):
	paginaobj = pdf1ler.getPage(pagina)
	pdfescreve.addPage(paginaobj)

# Itera sobre todas as páginas do arquivo em PDF
for pagina in range(pdf2ler.numPages):
	paginaobj = pdf2ler.getPage(pagina)
	pdfescreve.addPage(paginaobj)

# Escreve as páginas de ambos os arquivos em 'pdf_combinado.pdf'
pdfsaida = open('pdf_combinado.pdf', 'wb')
pdfescreve.write(pdfsaida)
pdfsaida.close()
pdf1.close()
pdf2.close()
