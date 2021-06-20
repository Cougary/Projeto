#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import send2trash 
import os

arquivo = input("Insert the file that you want to remove: ")
modo = input("Insert the desirable mode:\nType S for send2trash (Recoverable mode)\nType U to use unlink (Permanent remotion)\n")

if (modo == "S"):
	send2trash.send2trash(arquivo)
elif (modo == "U"):
	os.unlink(arquivo)
