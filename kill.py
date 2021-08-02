#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import os

processo = input("Digite o processo que deseja terminar: ")
os.system("killall " + str(processo))
