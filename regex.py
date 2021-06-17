#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import re

# Encontra padrões de texto em uma string 

texto = input("Digite o texto: ")
regex = re.compile(r'\d{7}-\d{4}')
mo = re.search(regex, texto)
print("Padrões encontrados: " + str(mo.group()))
