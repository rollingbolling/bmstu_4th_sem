from calcAlg import *

MENU_MAX = 3
MENU_MIN = 0

def printMenu():
    print("\n\033[1m{}\033[0m".format("Главное меню"))
    print("1. Найти решение системы уравнений")
    print("2. При заданном значении функции Лапласа найти её аргумент")
    print("3. Решить численно краевую задачу для дифференциального уравнения")
    print("0. Выход.")


def inputOption():
    opt = input("Введите номер пункта меню: ")
    is_correct = True
    try:
        opt = int(opt)
    except:
        is_correct = False
    if is_correct and (opt > MENU_MAX or opt < MENU_MIN):
        is_correct = False

    return is_correct, opt

def inputFloat(str):
    val = input(str)
    is_correct = True
    try:
        val = float(val)
    except:
        is_correct = False

    return is_correct, val


def inputInt(str):
    val = input(str)
    is_correct = True
    try:
        val = int(val)
    except:
        is_correct = False

    return is_correct, val


def main():
    opt = 1
    #print("ВА ЛР №5")
    while opt:
        printMenu()
        is_correct, opt = inputOption()
        while not is_correct:
            print("Ошибка! Введите целое число от {} до {}.".format(MENU_MIN, MENU_MAX))
            is_correct, opt = inputOption()

        if opt == 1:
            print("""
    ЗАДАЧА 1
    Найти решение системы уравнений
    x^2 + y^2 + z^2 = 1
    2x^2 + y^2 - 4z = 0
    3x^2 - 4y + z^2 = 0
                """)
            solveTask1()
        elif opt == 2:
            print("""
    ЗАДАЧА 2
    При заданном значении функции Лапласа найти её аргумент
    f(x) = (2 / sqrt(2 * pi)) ∫[0, x] exp(-t**2 / 2)dt
                """)
            is_correct, y = inputFloat("Введите значение функции: ")
            while not is_correct:
                print("Ошибка! Введите вещественное число.")
                is_correct, y = inputFloat("Введите значение функции: ")

            print("Result: {:.3}".format(solveTask2(y)))
        elif opt == 3:
            print("""
    ЗАДАЧА 3
    Решить численно краевую задачу для дифференциального уравнения
    y'' - y**3 = x**2, 0 <= x <= 1
    x = 0, y = 1,
    x = 1, y = 3
                """)
            is_correct, steps = inputInt("Введите кол-во шагов: ")
            while not is_correct:
                print("Ошибка! Введите целое число.")
                is_correct, steps = inputInt("Введите кол-во шагов: ")
            solveTask3(steps)

        elif opt == 0:
            print("Выход.")

main()
    

