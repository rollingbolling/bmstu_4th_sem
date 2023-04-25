import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import colorchooser, messagebox

from config import *
from draw import *
from dda import *
from brezenhem import *
from vu import *

def drawAxes():
    colour = "gray"
    canvasField.create_line(0, 3, CANVAS_W, 3, width=1, fill='gray', arrow=tk.LAST)
    canvasField.create_line(3, 0, 3, CANVAS_H, width=1, fill='gray', arrow=tk.LAST)
    for i in range(50, int(CANVAS_W), 50):
        canvasField.create_text(i, 15, text=str(abs(i)), fill=colour)
        canvasField.create_line(i, 0, i, 5, fill=colour)
    for i in range(50, int(CANVAS_H), 50):
        canvasField.create_text(15, i, text=str(abs(i)), fill=colour)
        canvasField.create_line(0, i, 5, i, fill=colour)

def clearScreen():
    canvasField.delete("all")
    drawAxes()

def drawLine():
    algorithm = algorithmsRB.get()
    x_start = xsEntry.get()
    y_start = ysEntry.get()
    x_end = xeEntry.get()
    y_end = yeEntry.get()

    if not x_start or not y_start:
        messagebox.showwarning("Input ERROR", "Не заданы координаты начала")
    elif not x_end or not y_end:
        messagebox.showwarning("Input ERROR", "Не заданы координаты конца")
    else:
        try:
            x_start, y_start = float(x_start), float(y_start)
            x_end, y_end = float(x_end), float(y_end)
        except all:
            messagebox.showwarning("Input ERROR", "Координаты неверны")

        if algorithm == 0:
            draw_line_by_algo(canvasField, DDA(x_start, y_start, x_end, y_end, colour=LINE_COLOUR))
        elif algorithm == 1: 
            draw_line_by_algo(canvasField, BrezenhemFloat(x_start, y_start, x_end, y_end, colour=LINE_COLOUR))
        elif algorithm == 2: 
            draw_line_by_algo(canvasField, BrezenhemInt(x_start, y_start, x_end, y_end, colour=LINE_COLOUR))
        elif algorithm == 3: 
            draw_line_by_algo(canvasField, BrezenhemSmooth(canvasField, x_start, y_start, x_end, y_end, LINE_COLOUR))
        elif algorithm == 4: 
            draw_line_by_algo(canvasField, VU(canvasField, x_start, y_start, x_end, y_end, fill=LINE_COLOUR))
        elif algorithm == 5:
            draw_line_stand_algo(canvasField, x_start, y_start, x_end, y_end, colour=LINE_COLOUR)
    
def drawSpector():
    algorithm = algorithmsRB.get()
    x_start = xsEntry.get()
    y_start = ysEntry.get()
    x_end = xeEntry.get()
    y_end = yeEntry.get()
    angle = angleEntry.get()

    if not x_start or not y_start:
        messagebox.showwarning("Input ERROR", "Не заданы координаты начала")
    elif not x_end or not y_end:
        messagebox.showwarning("Input ERROR", "Не заданы координаты конца")
    else:
        try:
            x_start, y_start = float(x_start), float(y_start)
            x_end, y_end = float(x_end), float(y_end)
            angle = float(angle)
        except all:
            messagebox.showwarning("Input ERROR", 'Координаты заданы неверно!')

        if algorithm == 0:
            draw_specter_by_algo(canvasField, DDA,
                                 x_start, y_start,
                                 x_end, y_end, angle,
                                 LINE_COLOUR)
        elif algorithm == 1:
            draw_specter_by_algo(canvasField, BrezenhemFloat,
                                 x_start, y_start,
                                 x_end, y_end, angle,
                                 LINE_COLOUR)
        elif algorithm == 2:
            draw_specter_by_algo(canvasField, BrezenhemInt,
                                 x_start, y_start,
                                 x_end, y_end, angle,
                                 LINE_COLOUR)
        elif algorithm == 3:
            draw_specter_by_algo(canvasField, BrezenhemSmooth,
                                 x_start, y_start,
                                 x_end, y_end, angle,
                                 LINE_COLOUR, intesive=True)
        elif algorithm == 4:
            draw_specter_by_algo(canvasField, VU,
                                 x_start, y_start,
                                 x_end, y_end, angle,
                                 LINE_COLOUR, intesive=True)
        elif algorithm == 5:
            draw_specter_stand_algo(canvasField, x_start, y_start, x_end, y_end, angle, LINE_COLOUR)

def timeInput():
    length = lengthEntry.get()
    try:
        length = int(length)
        if length <= 0:
            messagebox.showwarning("Input ERROR", "Длина для измерений должна быть больше нуля")
        else:
            time_bar(length)
    except ValueError:
        messagebox.showwarning("Input ERROR", "Длина для измерений задана неверно")

def stepInput():
    length = lengthEntry.get()
    try:
        length = int(length)
        if length <= 0:
            messagebox.showwarning("Input ERROR", "Длина для измерений должна быть больше нуля")
        else:
            step_bar(length)
    except ValueError:
        messagebox.showwarning("Input ERROR", "Длина для измерений задана неверно")
    
def close_plt():
    plt.figure("Исследование времени работы алгоритмов построения.",)
    plt.close()
    plt.figure("Исследование ступенчатости алгоритмов построение.")
    plt.close()

def time_bar(length):
    close_plt()

    plt.figure("Исследование времени работы алгоритмов построения.", figsize=(9, 7))
    times = list()
    angle = 1
    pb = [375, 200]
    pe = [pb[0] + length, pb[0]]

    times.append(draw_specter_by_algo(canvasField, DDA, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(draw_specter_by_algo(canvasField, BrezenhemFloat, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(draw_specter_by_algo(canvasField, BrezenhemInt, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(draw_specter_by_algo(canvasField, BrezenhemSmooth, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False, intesive=True))
    times.append(draw_specter_by_algo(canvasField, VU, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False, intesive=True))
    for i in range(len(times)):
        times[i] *= 100

    Y = range(len(times))

    L = ('ЦДА', 'Брезенхем с\nдействительными\nкоэффицентами',
         'Брезенхем с\nцелыми\nкоэффицентами', 'Брезенхем с\nс устранением\nступенчатости', 'Ву')
    plt.bar(Y, times, align='center')
    plt.xticks(Y, L)
    plt.ylabel("Cекунды (длина линии " + str(length) + ")")
    plt.show()

def step_bar(length):
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

    plt.figure("Исследование ступенчатости алгоритмов построение.", figsize=(18, 10))

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

root = tk.Tk()
root.title("Lab №3")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WINDOW_W = screen_width
WINDOW_H = screen_height

root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(False, False)

if __name__ == "__main__":
    # INPUT DATA FRAME


    dataFrame = tk.Frame(root)
    dataFrame["bg"] = FRAME_COLOUR

    dataFrame.place(x=BORDERS_SPACE, y=BORDERS_SPACE,
                    width=FRAME_W,
                    height=FRAME_H)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ВЫБОР АЛГОРИТМА

    algorithmsLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="АЛГОРИТМЫ ПОСТРОЕНИЯ",
                        font=("Consolas", 16),
                        fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    algorithmsArr = [("Цифровой дифференциальный анализатор", 0),
                    ("Брензенхем (float)", 1),
                    ("Брензенхем (integer)", 2),
                    ("Брензенхем (c устр. ступенчатости)", 3),
                    ("By", 4),
                    ("Библиотечная функция", 5)]
    algorithmsRB = tk.IntVar()

    for value in range(len(algorithmsArr)):
        tk.Radiobutton(dataFrame, variable=algorithmsRB, text=algorithmsArr[value][0], value=value, bg=str(MAIN_COLOUR_BUTON_BG),
                    indicatoron=False, font=("Consolas", 16), justify=tk.LEFT, highlightbackground="black",
                    ).place(x=10, y=(value + 1) * FRAME_H // COLUMNS, width=FRAME_W - 2 * BORDERS_SPACE, height=FRAME_H // COLUMNS)

    algorithmsLabel .place(x=0, y=0, width=FRAME_W, height=FRAME_H // COLUMNS)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ВЫБОР ЦВЕТА

    size_colour = (FRAME_W // 1.5) // 8

    colourChoiseLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА",
                        font=("Consolas", 16),
                        fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    
    colourChoiseLabel.place(x=0, y=8*FRAME_H // COLUMNS, width=FRAME_W, 
                            height=FRAME_H // COLUMNS)
    #-----------------------------------------------------------------------------------------------------------------------
    def get_colour_bg():
        colour = colorchooser.askcolor(title="Choose colour bg canvas")
        set_bgcolour(colour[-1])

    def set_bgcolour(colour):
        global CANVAS_COLOUR
        CANVAS_COLOUR = colour
        canvasField.configure(bg=CANVAS_COLOUR)

    colour_bg = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Выбор фона:", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)
    colour_bg.place(x=0, y=9 * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)
    
    white_bg = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_bgcolour("white"))
    yellow_bg = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_bgcolour("yellow"))
    orange_bg = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_bgcolour("orange"))
    red_bg = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_bgcolour("red"))
    purple_bg = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_bgcolour("purple"))
    lightgreen_bg = tk.Button(dataFrame, bg="lightgreen", activebackground="lightgreen", command=lambda: set_bgcolour("lightgreen"))
    green_bg = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_bgcolour("green"))
    lightblue_bg = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_bgcolour("lightblue"))
    
    white_bg.place(x=FRAME_W // 3 - BORDERS_SPACE, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    yellow_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    orange_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    red_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    purple_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    lightgreen_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    green_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    lightblue_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=9 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    
    bg_colour_change = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет BG", font=("Consolas", 16), command=get_colour_bg)
    bg_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=10 * FRAME_H // COLUMNS, width=FRAME_W // 1.5, height=FRAME_H // COLUMNS)
    #-----------------------------------------------------------------------------------------------------------------------
    def get_colour_line():
        colour = colorchooser.askcolor(title="Choose colour line")
        set_line_colour(colour[-1])
    
    def set_line_colour(colour):
        global LINE_COLOUR
        LINE_COLOUR = colour
        cur_colour_line.configure(bg=LINE_COLOUR)

    cur_colour_text_label = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Текущий цвет линии:",
                     font=("Consolas", 14),
                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_line = tk.Label(dataFrame, bg="black")
    cur_colour_text_label.place(x=FRAME_W // 3 - BORDERS_SPACE, y=13 * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=13 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    colour_line = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Выбор линии:", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)
    colour_line.place(x=0, y=11 * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)

    white_line = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_line_colour("white"))
    yellow_line = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_line_colour("yellow"))
    orange_line = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_line_colour("orange"))
    red_line = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_line_colour("red"))
    purple_line = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_line_colour("purple"))
    lightgreen_line = tk.Button(dataFrame, bg="lightgreen", activebackground="lightgreen", command=lambda: set_line_colour("lightgreen"))
    green_line = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_line_colour("green"))
    lightblue_line = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_line_colour("lightblue"))
    
    white_line.place(x=FRAME_W // 3 - BORDERS_SPACE, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    yellow_line.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    orange_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    red_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    purple_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    lightgreen_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    green_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)
    lightblue_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=11 * FRAME_H // COLUMNS, width=size_colour, height=FRAME_H // COLUMNS)

    line_colour_change = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет LINE", font=("Consolas", 16), command=get_colour_line)
    line_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=12 * FRAME_H // COLUMNS, width=FRAME_W // 1.5, height=FRAME_H // COLUMNS)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # DRAW LINE
    lineMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ЛИНИИ",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    argumnetsLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Xн         Yн         Xк          Yк",
                        font=("Consolas", 14),
                        fg=MAIN_COLOUR_LABEL_TEXT)

    xsEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ysEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    xeEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    yeEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    drawLineBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить линию", font=("Consolas", 14),
                             command=drawLine)


    lineMakeLabel.place(x=0, y=14 * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    argumnetsLabel.place(x=0, y=15 * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    xsEntry.place(x=0, y=16 * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ysEntry.place(x=FRAME_W // 4, y=16 * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    xeEntry.place(x=2 * FRAME_W // 4, y=16 * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    yeEntry.place(x=3 * FRAME_W // 4, y=16 * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    drawLineBtn.place(x=FRAME_W // 2 / 2.5, y=18 * FRAME_H // COLUMNS, width=FRAME_W // 1.5, height=FRAME_H // COLUMNS)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # DRAW SPECTOR
    lineColourLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Угол поворота (в градуссах):",
                        font=("Consolas", 14),
                        fg=MAIN_COLOUR_LABEL_TEXT)
    angleEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    drawSpnBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр", font=("Consolas", 14),
                        command=drawSpector)

    lineColourLabel.place(x=0, y=17 * FRAME_H // COLUMNS, width=3 * FRAME_W // 4, height=FRAME_H // COLUMNS)
    angleEntry.place(x=3 * FRAME_W // 4, y=17 * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    drawSpnBtn.place(x=FRAME_W // 2 / 2.5, y=19 * FRAME_H // COLUMNS, width=FRAME_W // 1.5, height=FRAME_H // COLUMNS)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # INFO & STATS
    def show_info():
        messagebox.showinfo('Информация',
                            'С помощью данной программы можно построить отрезки 6 способами:\n'
                            '1) методом цифрового дифференциального анализатора;\n'
                            '2) методом Брезенхема с действитльными коэфициентами;\n'
                            '3) методом Брезенхема с целыми коэфициентами;\n'
                            '4) методом Брезенхема с устранением ступенчатости;\n'
                            '5) методом Ву;\n'
                            '6) стандартым методом.\n'
                            '\nДля построения отрезка необходимо задать его начало\n'
                            'и конец и выбрать метод построения из списка предложенных.\n'
                            '\nДля построения спектра (пучка отрезков)\n'
                            'необходимо задать начало и конец,\n'
                            'выбрать метод для построения,\n'
                            'а также угол поворота отрезка.\n'
                            '\nДля анализа ступенчатости достаточно нажать на кнопку "Сравнение ступенчатости".\n'
                            'Анализ ступенчатости и времени исполнения приводится\n'
                            'в виде графиков pyplot.\n'
                            'Введите длину отрезка, если хотите сделать анализ программы\n'
                            'при построении отрезков определенной длины.')


    lineLengthLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Длина линии:",
                        font=("Consolas", 14),
                        fg=MAIN_COLOUR_LABEL_TEXT)
    lengthEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")

    compareTimenBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Сравнения времени", font=("Consolas", 14),
                                command=timeInput)
    compareGradationBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Сравнения ступенчатости", font=("Consolas", 14),
                                    command=stepInput)
    clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=clearScreen)
    infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14),
                        command=show_info)

    lineLengthLabel.place(x=0, y=22 * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)
    lengthEntry.place(x=FRAME_W // 3, y=22 * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)
    compareTimenBtn.place(x=20, y=23 * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    compareGradationBtn.place(x=20, y=24 * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    clearCanvasBtn.place(x=20, y=25 * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    infoBtn.place(x=20, y=26 * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # CANVAS
    canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
    canvasField.place(x=WINDOW_W * FRAME_SITUATION + BORDERS_SPACE, y=BORDERS_SPACE,
                      width=CANVAS_W, height=CANVAS_H)
    drawAxes()
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------


root.mainloop()