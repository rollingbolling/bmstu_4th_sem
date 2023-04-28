from config import *
from dda import *
from vu import *
from brezenhem import *
from draw import *
import matplotlib.pyplot as plt
import numpy as np

def close_plt():
    plt.figure("Исследование времени работы алгоритмов")
    plt.close()
    plt.figure("Исследование ступенчатости работы алгоритмов")
    plt.close()

def time_bar(length, canvasField):
    close_plt()
    plt.figure("Исследование времени работы алгоритмов", figsize=(PLOT_W, PLOT_H))
    print(PLOT_W, PLOT_H)
    times = list()
    angle = 1
    pb = [375, 200]
    pe = [pb[0] + length, pb[0]]

    times.append(draw_specter_by_algo(canvasField, DDA, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(
        draw_specter_by_algo(canvasField, BrezenhemFloat, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(
        draw_specter_by_algo(canvasField, BrezenhemInt, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(
        draw_specter_by_algo(canvasField, BrezenhemSmooth, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False,
                             intesive=True))
    times.append(draw_specter_by_algo(canvasField, VU, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False,
                                      intesive=True))
    for i in range(len(times)):
        times[i] *= 100

    Y = range(len(times))

    L = ('ЦДА', 'Брезенхем с\nдействительными\nкоэффицентами',
         'Брезенхем с\nцелыми\nкоэффицентами', 'Брезенхем с\nс устранением\nступенчатости', 'Ву')
    plt.bar(Y, times, align='center')
    plt.xticks(Y, L)
    plt.ylabel("Cекунды (длина линии " + str(length) + ")")
    plt.show()

def step_bar(length, canvasField):
    close_plt()

    angle = 0
    step = 2
    pb = [0, 0]
    pe = [pb[0], pb[1] + length]

    angles = []
    DDA_steps = []
    BrezenhemInteger_steps = []
    BrezenhemFloat_steps = []
    BrezenhemSmooth_steps = []
    VU_steps = []

    for j in range(90 // step):
        DDA_steps.append(DDA(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemInteger_steps.append(BrezenhemInt(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemFloat_steps.append(BrezenhemFloat(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemSmooth_steps.append(BrezenhemSmooth(canvasField, pb[0], pb[1], pe[0], pe[1], stepmode=True))
        VU_steps.append(VU(canvasField, pb[0], pb[1], pe[0], pe[1], stepmode=True))

        pe[0], pe[1] = turn_point(radians(step), pe[0], pe[1], pb[0], pb[1])
        angles.append(angle)
        angle += step

    plt.figure("Исследование ступенчатости алгоритмов построение.", figsize=(PLOT_W, PLOT_H))

    plt.subplot(2, 3, 1)
    plt.plot(angles, DDA_steps, label="ЦДА")
    plt.plot(angles, BrezenhemInteger_steps, '--', label="Брензенхем с целыми или\nдействительными коэффицентами")
    plt.plot(angles, BrezenhemInteger_steps, '.', label="Брензенхем с устр\nступенчатости")
    plt.plot(angles, VU_steps, '-.', label="By")
    plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(length))
    plt.xticks(np.arange(91, step=5))
    plt.legend()
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 2)
    plt.title("ЦДА")
    plt.plot(angles, DDA_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 3)
    plt.title("BУ")
    plt.plot(angles, VU_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 4)
    plt.title("Брензенхем с действительными коэффицентами")
    plt.plot(angles, BrezenhemFloat_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 5)
    plt.title("Брензенхем с целыми коэффицентами")
    plt.plot(angles, BrezenhemInteger_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 6)
    plt.title("Брензенхем с устр. ступенчатости")
    plt.plot(angles, BrezenhemSmooth_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.show()

