#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import time, sys

lista = []

# Define uma função
def amostra():
    while True:
        elementos = int(input("Digite os numeros ou '0' para sair do programa: "))
        if (elementos == 0):
            break
            sys.exit()
        lista.append(elementos) 
        tamanho = len(lista)
        print("Tamanho da lista: " + str(tamanho))
        for elemento in lista:
            print(elemento)
 
inicio = time.time()
amostra()
final = time.time()
sub = inicio - final
print("Tempo de execução da função: " + str(sub))
        
