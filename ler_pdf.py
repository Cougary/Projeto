#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2, os

print("Diretório corrente: " + str(os.getcwd()))
novo_dir = os.chdir('/home/winner/Downloads')
pdf = open('Al Sweigart - Automate the Boring Stuff with Python_ Practical Programming for Total Beginners-No Starch Press (2015).pdf', 'rb')
pdfler = PyPDF2.PdfFileReader(pdf)
print("Verificando se o PDF está criptografado...")
if (pdfler.isEncrypted == True):
	print("O PDF está criptografado. Não será possível realizar a sua leitura!")
else:
	print("Número de páginas do PDF: " + str(pdfler.numPages))
	pagina = int(input("Digite a página que deseja ler: "))
	page = pdfler.getPage(pagina)
	print("Página: ")
	print(page.extractText())
