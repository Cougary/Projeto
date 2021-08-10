#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import time, sys

if len(sys.argv) < 1:
    print("Uso: cron_pretty.py <nome>")

def imprime():
    for letra in sys.argv[1]:
        print(letra)

inicio = time.time()
imprime()
final = time.time()
sub = inicio - final
sub_text = str(sub)
print("Lap #: " + sub_text.rjust(20, "*"))
