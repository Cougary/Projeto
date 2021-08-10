#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import smtplib, getpass

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
senha = getpass.getpass("Digite a senha de seu e-mail: ")
smtpObj.login('fourtinet@gmail.com', senha)
smtpObj.sendmail('fourtinet@gmail.com', 'fourtinet@gmail.com', 'Subject: Assunto!\n.\n Mensagem!')
smtpObj.quit()
