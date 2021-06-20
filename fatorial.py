#!/usr/bin/env python3
#!-*-coding:utf-8-*-

numero = int(input("Digite o número: ")) 

total = 1
while (numero > 1):
	total *= numero
	numero = numero - 1
	print(numero)
	
print("Total: " + str(total))
