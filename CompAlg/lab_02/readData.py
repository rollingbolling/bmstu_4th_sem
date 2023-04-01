from pointClass import *
from numpy import linspace

EPS = 1e-6

def f(x):
    return x**3 

def generateTable(sx, ex, amx):
    dataTable = list()
    xValues = linspace(sx, ex, amx)

    for i in range(amx):
        dataTable.append(Point(xValues[i], f(xValues[i])))

    return dataTable

def readTable(filename):
    dataTable = list()
    file = open(filename)
    
    for line in file.readlines():
        row = list(map(float, line.split(" ")))
        dataTable.append(Point(row[0], row[1]))

    file.close()
    return dataTable

def printTable(dataTable):
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")
    print("| {:^5s} | {:^10s} | {:^10s} |".format("№", "X", "Y", "Y\'"))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")
    for i in range(len(dataTable)):
        print("| {:^5d} | {:^10.3f} | {:^10.3f} |".format(i, dataTable[i].x, dataTable[i].y))
    print("+" + "-" * 7 + ("+" + "-" * 12) * 2 + "+")
