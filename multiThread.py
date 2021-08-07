#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import threading, time

def ping():
    for i in range(10):
        time.sleep(1)
        print(str(i) + str(i) + str(i) + str(i) + str(i))

def pong():
    valor = 10
    for i in range(1, 10):
        time.sleep(1)
        valor -= 1
        print("\t\t" + str(valor) + str(valor) + str(valor) + str(valor) + str(valor))

threadObj1 = threading.Thread(target=ping)
threadObj1.start()

threadObj2 = threading.Thread(target=pong)
threadObj2.start()


