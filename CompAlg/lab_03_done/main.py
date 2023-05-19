from read_data import *
from multidimensional_interpolation import *


def main():
    data = read_table('data.txt')

    x = float(input('Введите значение x: '))
    y = float(input('Введите значение y: '))
    z = float(input('Введите значение z: '))
    print()

    nx = int(input('Введите степень интерполяции Nx: '))
    ny = int(input('Введите степень интерполяции Ny: '))
    nz = int(input('Введите степень интерполяции Nz: '))
    print()

    x_dir = int(
        input('Выберите метод интерполяции по х (1 - полином Ньютона, 2 - сплайны): '))
    y_dir = int(
        input('Выберите метод интерполяции по y (1 - полином Ньютона, 2 - сплайны): '))
    z_dir = int(
        input('Выберите метод интерполяции по z (1 - полином Ньютона, 2 - сплайны): '))
    print()

    x_dir = get_method(x_dir)
    y_dir = get_method(y_dir)
    z_dir = get_method(z_dir)

    print("Результат интерполяции:")
    print(
        f'Полиномы Ньютона: {multi_interpolation(data, nx, ny, nz, x, y, z):.2f}')
    print(
        f'Сплайны: {multi_interpolation(data, nx, ny, nz, x, y, z, SPLINE, SPLINE, SPLINE):.2f}')
    print(
        f'Пользовательский вариант: {multi_interpolation(data, nx, ny, nz, x, y, z, x_dir, y_dir, z_dir): .2f}')


def get_method(method_numb):
    return NEWTON if method_numb == 1 else SPLINE


if __name__ == '__main__':
    main()
