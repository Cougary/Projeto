#!/usr/bin/env python3
#!-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Navega até o site
browser = webdriver.Firefox()
browser.get('https://github.com/')

# Define os dados cadastrais: Email e Senha para login
login = browser.find_element_by_link_text('Sign in')
login.click()
usuario = browser.find_element_by_id('login_field')
user = input("Digite seu email: ")
usuario.send_keys(user)
senha = browser.find_element_by_id('password')
passg = input("Digite sua senha: ")
senha.send_keys(passg)

# Envia os dados
senha.submit()

