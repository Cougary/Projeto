#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import docx

lista = [] 

def ler_arquivo():
    arquivo = open('guests.txt', 'r')
    for linha in arquivo:
        print(linha)
        lista.append(linha)
    arquivo.close()

ler_arquivo()

def cria_docx():
    doc = docx.Document()
    for elemento in lista:
        doc.add_paragraph(elemento)
    doc.save('convidados.docx')

cria_docx()
