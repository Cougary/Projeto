#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2

arquivo = input("Digite o PDF que quer criptografar: ")
pdf = open(arquivo, 'rb')
pdfler = PyPDF2.PdfFileReader(pdf)
pdfescreve = PyPDF2.PdfFileWriter()

for pagina in range(pdfler.numPages):
	pdfescreve.addPage(pdfler.getPage(pagina))

senha = input("Digite a senha que deseja usar: ")
pdfescreve.encrypt(senha)
pdfsaida = open('criptografado.pdf', 'wb')
pdfescreve.write(pdfsaida)
pdfsaida.close()
pdf.close()
