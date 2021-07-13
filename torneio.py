#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import sys 
import os

print("-" * 18)
print("CAMPEONATO FUTEBOL")
print("-" * 18)

time1 = input("Nome do 1o. time: ")
time2 = input("Nome do 2o. time: ")
time3 = input("Nome do 3o. time: ")

os.system('clear')
print("-" * 18)
print("TABELA DE PARTIDAS")
print("-" * 18)
lista = [time1, time2, time3]
lista2 = [time1, time2, time3]
for time in lista:
	for team in lista2:
		if (time == team):
			continue
		else:
			print(time + "\t [] x [] " + team)



