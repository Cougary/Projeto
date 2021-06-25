#!/usr/bin/env python3
#!-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
elemento = browser.find_element_by_tag_name('html')

while(True):
	elemento.send_keys(Keys.UP)
	elemento.send_keys(Keys.DOWN)
	elemento.send_keys(Keys.RIGHT)
	elemento.send_keys(Keys.LEFT)
	
	

	


