#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import subprocess

arquivo = input("Digite o arquivo que deseja rodar: ")
subprocess.Popen(['/usr/bin/python3', arquivo])
