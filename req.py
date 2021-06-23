#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import requests
import sys

site = input("Digite o site que deseja baixar aqui: ")
req = requests.get(site)
print("Tamanho: " + str(len(req.text)))
print(req.text)
