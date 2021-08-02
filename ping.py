#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import time

def ping():
    for i in range(100):
        print(" " + str(i)+ "\t" + str(i) + "\t" + str(i) + "\t" + str(i) + "\t" + str(i) + "\t" + str(i) + "\t" + str(i))
        time.sleep(0.2)

ping()
        
