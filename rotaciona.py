#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import PyPDF2

pdf = open('atividadeum.pdf', 'rb')
pdfler = PyPDF2.PdfFileReader(pdf)
pagina = pdfler.getPage(0)
pagina.rotateClockwise(90)

pdfescreve = PyPDF2.PdfFileWriter()
pdfescreve.addPage(pagina)
pdfsaida = open('rotacionado.pdf', 'wb')
pdfescreve.write(pdfsaida)
pdfsaida.close()
pdf.close()

