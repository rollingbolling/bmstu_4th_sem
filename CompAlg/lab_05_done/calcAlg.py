import numpy as np
import math as m
from prettytable import PrettyTable
import matplotlib.pyplot as plt

EPS = 1e-6

def solveTask1():
    """
    ЗАДАЧА 1
    Найти решение системы уравнений
    x^2 + y^2 + z^2 = 1
    2x^2 + y^2 - 4z = 0
    3x^2 - 4y + z^2 = 0
    """

    # Начальное приближение
    x = [1, 1, 1]

    # Функции
    def f(xArr):
        f = np.array([[xArr[0]**2 + xArr[1]**2 + xArr[2]**2 - 1],
            [2 * xArr[0]**2 + xArr[1]**2 - 4 * xArr[2]],
            [3 * xArr[0]**2 - 4 * xArr[1] + xArr[2]**2]])
        return f

    # Матрица Якоби
    def w(xArr):
        w = np.array([[2 * xArr[0], 2 * xArr[1], 2 * xArr[2]],
            [4 * xArr[0], 2 * xArr[1], -4],
            [6 * xArr[0], -4, 2 * xArr[2]]])
        return w

    
    f_matr = f(x)
    w_matr = w(x)

    print("До начала итераций:")
    print("Система:")
    for item in f_matr:
        for el in item:
            print(el, end=" ")
        print()

    print("Матрица Якоби:")
    for item in w_matr:
        for el in item:
            print(el, end=" ")
        print()

    deltaX = [1, 1, 1]
    xPrev = []

    def divArr(arr1, arr2):
        res = []
        for i in range(len(arr1)):
            res.append(arr1[i] / arr2[i])
        return res

    def stopIter(arr, eps):
        res = True
        for i in range(len(arr)):
            if abs(arr[i]) >= eps:
                res = False
                break
        return res
    
    def subArr(arr1, arr2):
        res = []
        for i in range(len(arr1)):
            res.append(arr1[i] - arr2[i])
        return res

    while not stopIter(divArr(deltaX, x), EPS):
        xPrev = x.copy()
        x = subArr(xPrev, np.dot(np.linalg.inv(w_matr), f_matr).flatten())
        w_matr = w(x)
        f_matr = f(x)
        deltaX = subArr(x, xPrev)

    tableCols = ["X", "Y", "Z"]
    tableRows = [["{:.3}".format(x[0]), "{:.3}".format(x[1]), "{:.3}".format(x[2])]]

    printResTable(tableCols, tableRows)
    return x

#print(solveTask1())
#print()

def solveTask2(y):#, xA, xB, stepsCount):
    """
    ЗАДАЧА 2
    При заданном значении функции Лапласа найти её аргумент
    f(x) = (2 / sqrt(2 * pi)) ∫[0, x] exp(-t**2 / 2)dt
    """
    #, -10, 10, 100
    xA = -10
    xB = 10
    stepsCount = 200
    def trapezoidal_rule(f, a, b, n):
        # Mетод трапеций
        h = (b - a) / n
        sum = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            x = a + i * h
            sum += f(x)
        return h * sum

    def laplaceFunc(x, steps):
        def func(t):
            return m.exp(-(t**2 / 2))

        return (2 / m.sqrt(2 * m.pi)) * trapezoidal_rule(func, 0, x, steps)

    # Метод половинного деления
    while abs(xB - xA) > EPS:
        c = (xA + xB) / 2
        check = (laplaceFunc(xB, stepsCount) - y) * (laplaceFunc(c, stepsCount) - y)
        if (check < 0):
            xA = c
        elif (check > 0):
            xB = c
        else:
            return (xA + xB) / 2

    return (xA + xB) / 2


def solveTask3(steps):
    """
    ЗАДАЧА 3
    Решить численно краевую задачу для дифференциального уравнения
    y'' - y**3 = x**2, 0 <= x <= 1
    x = 0, y = 1,
    x = 1, y = 3
    """
    x1, x2 = 0, 1
    y1, y2 = 1, 3
    # Вводим разностную сетку
    h = (x2 - x1) / steps # 1 / steps
    xArr = [x1 + i * h for i in range(steps + 1)]

    print("Шаг = {:.3}".format(h))
    if len(xArr) <= 10:
        print("Разностная сетка:\n", xArr)
        print("Длина = ", len(xArr))

    # Аппроксимируем вторую производную разностным аналогом
    # Yn-1 - 2 * Yn - h**2 * Yn**3 + Yn+1 = h**2 * x**2
    # Y0 = 1
    # Yn = 3
    # Решаем методом Ньютона
    # Начальное приближение
    yArr = [y1 + i * (y2 - y1) / steps for i in range(1, steps)]
    yArr = [y1] + yArr
    yArr += [y2]

    if len(yArr) <= 10:
        print("Начальное приближение:\n", yArr)
        print("Длина = ", len(yArr))

    # Функции
    def f(xArr, yArr, h):
        f = []
        f.append([0])
        for i in range(1, len(yArr) - 1):
            f.append([yArr[i - 1] - 2 * yArr[i] - h**2 * 
                    yArr[i]**3 + yArr[i + 1] - h**2 * xArr[i]])
        f.append([0])

        f = np.array(f)
        return f

    # Матрица Якоби
    def w(yArr, h):
        w = []
        w.append([1 if i == 0 else 0 for i in range(len(yArr))])
        for i in range(1, len(yArr) - 1): # w loop
            tmp = []
            for j in range(len(yArr)): # y loop
                if j == i - 1:
                    tmp.append(1)
                elif j == i:
                    tmp.append(-2 - h**2 * 3 * yArr[j]**2)
                elif j == i + 1:
                    tmp.append(1)
                else:
                    tmp.append(0)
            w.append(tmp.copy())

        w.append([1 if i == len(yArr) - 1 else 0 for i in range(len(yArr))])
        w = np.array(w)

        return w
    
    f_matr = f(xArr, yArr, h)
    w_matr = w(yArr, h)

    deltaY = [y1 + i * (y2 - y1) / steps for i in range(1, steps)]
    deltaY = [y1] + deltaY
    deltaY += [y2]

    if len(f_matr) <= 10:
        print("До начала итераций:")
        print("Система:")
        for item in f_matr:
            for el in item:
                print(el, end=" ")
            print()

    if len(w_matr) <= 10:
        print("Матрица Якоби:")
        for item in w_matr:
            for el in item:
                print(round(el, 4), end=" ")
            print()


    def divArr(arr1, arr2):
        res = []
        for i in range(len(arr1)):
            res.append(arr1[i] / arr2[i])
        return res


    def stopIter(arr, eps):
        res = True
        for i in range(len(arr)):
            if abs(arr[i]) >= eps:
                res = False
                break
        return res


    def subArr(arr1, arr2):
        res = []
        for i in range(len(arr1)):
            res.append(arr1[i] - arr2[i])
        return res

    yPrev = []
    while not stopIter(divArr(deltaY, yArr), EPS):
        yPrev = yArr.copy()
        yArr = subArr(yPrev, np.dot(np.linalg.inv(w_matr), f_matr).flatten())

        f_matr = f(xArr, yArr, h)
        w_matr = w(yArr, h)

        deltaY = subArr(yArr, yPrev)


    tableCols = ["Xn", "Yn"]
    tableRows = []
    for i in range(1, len(xArr) - 1):
        tableRows.append(["{:.3}".format(xArr[i]), "{:.3}".format(yArr[i])])

    printResTable(tableCols, tableRows)
    showPlot(xArr, yArr, h)


def printResTable(cols, rows):
    table = PrettyTable()
    table.field_names = cols
    for item in rows:
        table.add_row(item)
    print(table)

def showPlot(xArr, yArr, h):
    plt.plot(xArr, yArr)
    plt.grid()
    plt.text(0, yArr[-1], "$h = {:.3}$".format(h))
    plt.show()


#solveTask3(100)

