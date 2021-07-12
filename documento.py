#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import docx

doc = docx.Document()
texto = input("Digite o texto que deseja inserir no documento Word: ")
doc.add_paragraph(texto)
nome = input("Digite o nome do documento: ")
doc.save(nome)
