#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2, os

arquivo = input("Digite o arquivo PDF que deseja descriptografar com o path absoluto: ")
senha = input("Digite a senha para descriptografia: ")
pdf = PyPDF2.PdfFileReader(open(arquivo, 'rb'))
print("Está criptografado? " + str(pdf.isEncrypted))
pdf.decrypt(senha)

print("Número de páginas do PDF: " + str(pdf.numPages))
numero = int(input("Digite o número da página que deseja ler: "))
pagina = pdf.getPage(numero)
print("Texto da página: " + str(pagina.extractText()))
