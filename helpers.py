'''funciones de ayuda'''
import os
import platform


def clear():
    if platform.system()=="windows":
        os.system('cls')
    else:
        os.system('clear')
        