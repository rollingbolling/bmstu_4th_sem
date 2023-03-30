import FileFuncs as F_func
from polynom import *

if __name__ == "__main__":
    pointTable = F_func.readTable("./data.txt")
    monotone = getTypeOfMonotone(pointTable)
    pointTable.sort(key=lambda point: point.x)

    F_func.printTable(pointTable)

    x = float(input("Введите x: "))
    n = int(input("Введите n: "))

    index = getIndex(pointTable, x)
    newPointTable = getWorkingPoints(pointTable, index, n + 1)
    subsNewton = NewtonMethod(newPointTable)
    subsHermit = HermitMethod(newPointTable)
    print("Newton:")
    printSubTable(subsNewton)
    print("Hermit:")
    printSubTable(subsHermit)

    print("Newton: {:.6f}".format(calcApproxValue(subsNewton, n, x)))
    print("Hermit: {:.6f}".format(calcApproxValue(subsHermit, n, x)))

    print("Root by Newton: {:.6f}".format(rootByNewton(pointTable, n, monotone)))
    print("Root by Hermit: {:.6f}".format(rootByHermit(pointTable, n, monotone)))