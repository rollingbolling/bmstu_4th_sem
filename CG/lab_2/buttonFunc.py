import tkinter as tk
import tkinter.messagebox as mb
import config as cfg

INFORMATION = "Функциональность программы"

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def showInfoParams():
    mb.showinfo("Info", INFORMATION)

