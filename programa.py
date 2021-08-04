#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import time, os, sys, webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def inicia():
    print("O programa irá iniciar em 10 segundos")
    for i in range(1,10):
        print(i)
        time.sleep(1)

inicia()

def caixa():
    print("CAIXA MÁGICA!")
    for i in range(10):
        print("*" * 30)

while True:
    print("[1] Caixa Mágica")
    print("[2] Listagem do Diretório")
    print("[3] Remoção de algum arquivo")
    print("[4] Executar o Neofetch")
    print("[5] Web Scrapping")
    print("[6] Sair do programa")
    escolha = int(input("Digite o programa que deseja escolher: "))

    if (escolha == 1):
        caixa()
    elif (escolha == 2):
        caminho = os.getcwd()
        diretorio = os.listdir(caminho)
        print("Listagem: ")
        for arquivo in diretorio:
            print(arquivo)
    elif (escolha == 3):
        arq = input("Digite o arquivo que deseja remover: ")
        os.unlink(arq)
        print("Arquivo removido!")
    elif (escolha == 4):
        print("Neofetch: ")
        os.system("neofetch")
    elif (escolha == 5):
        site = input("Digite o site que deseja abrir: ")
        webbrowser.open(site)
    elif (escolha == 6):
        break
        sys.exit()
    else:
        print("Digite uma opção válida!")



