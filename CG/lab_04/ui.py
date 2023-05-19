import tkinter as tk
from tkinter import colorchooser, messagebox

from config import *


def place_bg_colour_choice(frame, canvas, size_colour, start_column):
    def get_colour_bg():
        colour = colorchooser.askcolor(title="Choose colour bg canvas")
        set_bg_colour(colour[-1])

    def set_bg_colour(colour):
        global CANVAS_COLOUR
        CANVAS_COLOUR = colour
        canvas.configure(bg=CANVAS_COLOUR)

    colour_bg = tk.Label(frame, bg=FRAME_COLOUR, text="Фон:", font=("Consoles", FONT_LABEL),
                         fg=MAIN_COLOUR_LABEL_TEXT)
    colour_bg.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)

    white_bg = tk.Button(frame, bg="white", activebackground="white", command=lambda: set_bg_colour("white"))
    yellow_bg = tk.Button(frame, bg="yellow", activebackground="yellow", command=lambda: set_bg_colour("yellow"))
    orange_bg = tk.Button(frame, bg="orange", activebackground="orange", command=lambda: set_bg_colour("orange"))
    red_bg = tk.Button(frame, bg="red", activebackground="red", command=lambda: set_bg_colour("red"))
    purple_bg = tk.Button(frame, bg="purple", activebackground="purple", command=lambda: set_bg_colour("purple"))
    light_green_bg = tk.Button(frame, bg="light green", activebackground="light green",
                               command=lambda: set_bg_colour("light green"))
    green_bg = tk.Button(frame, bg="green", activebackground="green", command=lambda: set_bg_colour("green"))
    light_blue_bg = tk.Button(frame, bg="light blue", activebackground="light blue",
                              command=lambda: set_bg_colour("light blue"))

    white_bg.place(x=FRAME_W // 3 - BORDERS_SPACE, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                   height=FRAME_H // COLUMNS)
    yellow_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                    height=FRAME_H // COLUMNS)
    orange_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                    height=FRAME_H // COLUMNS)
    red_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                 height=FRAME_H // COLUMNS)
    purple_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                    height=FRAME_H // COLUMNS)
    light_green_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                         height=FRAME_H // COLUMNS)
    green_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                   height=FRAME_H // COLUMNS)
    light_blue_bg.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)

    bg_colour_change = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет BG",
                                 font=("Consoles", FONT_BUTTON), command=get_colour_bg)
    bg_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                           height=FRAME_H // COLUMNS)


def place_algo_choose(frame, algorithms_rb, start_column):
    algorithms_label = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="АЛГОРИТМЫ ПОСТРОЕНИЯ",
                                font=("Consoles", FONT_HEAD),
                                fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    algorithms_arr = [("Каноническое уравнение", 0),
                      ("Параметрическое уравнение", 1),
                      ("Алгоритм средней точки", 2),
                      ("Алгоритм Брензенхема", 3),
                      ("Библиотечная функция", 4)]

    for value in range(len(algorithms_arr)):
        tk.Radiobutton(frame, variable=algorithms_rb, text=algorithms_arr[value][0], value=value,
                       bg=str(MAIN_COLOUR_BUTON_BG),
                       indicatoron=False, font=("Consoles", FONT_BUTTON), justify=tk.LEFT, highlightbackground="black",
                       ).place(x=10, y=(start_column + value + 1) * FRAME_H // COLUMNS, width=FRAME_W - 2 * BORDERS_SPACE,
                               height=FRAME_H // COLUMNS)

    algorithms_label.place(x=0, y=start_column, width=FRAME_W, height=FRAME_H // COLUMNS)


def place_draw_figure_block(frame, xcEntry, ycEntry, circle_radEntry, ellipse_wEntry, ellipse_hEntry, drawCircleBtn, drawEllipseBtn, start_column):
    circleMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ФИГУРЫ",
                               font=("Consoles", FONT_HEAD),
                               fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    argumentsLabel = tk.Label(frame, bg=FRAME_COLOUR,
                              text=("X{0}Y".format(" " * int(FRAME_W // 1.5 // FONT_LABEL))),
                              font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT)

    circleMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    argumentsLabel.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    xcEntry.place(x=0, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    ycEntry.place(x=FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawCircleBtn.place(x=0, y=(start_column + 6) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawEllipseBtn.place(x=FRAME_W // 2, y=(start_column + 6) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

    circleLabel = tk.Label(frame, bg=FRAME_COLOUR, text="Окружность", font=("Consoles", FONT_LABEL),
                           fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ellipseLabel = tk.Label(frame, bg=FRAME_COLOUR, text="Эллипс", font=("Consoles", FONT_LABEL),
                            fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    circleLabel.place(x=0, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    ellipseLabel.place(x=FRAME_W // 2, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

    circle_radLabel = tk.Label(frame, bg=FRAME_COLOUR, text="Радиус:", font=("Consoles", FONT_LABEL),
                               fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ellipse_wLabel = tk.Label(frame, bg=FRAME_COLOUR, text="Ширина:", font=("Consoles", FONT_LABEL),
                              fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ellipse_hLabel = tk.Label(frame, bg=FRAME_COLOUR, text="Высота:", font=("Consoles", FONT_LABEL),
                              fg=MAIN_COLOUR_LABEL_TEXT, justify="center")

    circle_radLabel.place(x=0, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    circle_radEntry.place(x=FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wLabel.place(x=2 * FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wEntry.place(x=3 * FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hLabel.place(x=2 * FRAME_W // 4, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hEntry.place(x=3 * FRAME_W // 4, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)


def place_draw_spectre_block(dataFrame, circle_radEntry, ellipse_hEntry, ellipse_wEntry, figureAmountEntry, figureStepEntry, drawSpecCircleBtn, drawSpecEllipseBtn, start_column):
    spectreMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ СПЕКТРА",
                                font=("Consoles", FONT_HEAD),
                                fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    spectreMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    circle_radLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Радиус:", font=("Consoles", FONT_LABEL),
                               fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ellipse_wLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Ширина:", font=("Consoles", FONT_LABEL),
                              fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ellipse_hLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Высота:", font=("Consoles", FONT_LABEL),
                              fg=MAIN_COLOUR_LABEL_TEXT, justify="center")

    circle_radLabel.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    circle_radEntry.place(x=FRAME_W // 4, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wLabel.place(x=2 * FRAME_W // 4, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wEntry.place(x=3 * FRAME_W // 4, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hLabel.place(x=2 * FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hEntry.place(x=3 * FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)

    figureAmountLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Кол-во измен.:", font=("Consoles", FONT_LABEL),
                                 fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    figureStepLabel = tk.Label(dataFrame, bg=FRAME_COLOUR, text="Шаг измен.:", font=("Consoles", FONT_LABEL),
                               fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    
    figureStepLabel.place(x=0, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureStepEntry.place(x=FRAME_W // 2, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureAmountLabel.place(x=0, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureAmountEntry.place(x=FRAME_W // 2, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

    drawSpecCircleBtn.place(x=0, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawSpecEllipseBtn.place(x=FRAME_W // 2, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)


def place_analys_block(frame, compareCircleTimeBtn, compareSpecTimeBtn, start_column):
    StatsLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="АНАЛИЗ",
                          font=("Consolas", FONT_HEAD),
                          fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    StatsLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    compareCircleTimeBtn.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    compareSpecTimeBtn.place(x=FRAME_W // 2, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)


def place_clear_info_block(frame, clear_screen, start_column):
    def show_info():
        messagebox.showinfo('Информация',
                        'С помощью данной программы можно построить окружность или эллипс 5-ми способами:\n'
                        '1) используя Каноническое уравнение;\n'
                        '2) используя Параметрическое уравнение;\n'
                        '3) Алгоритм средней точки;\n'
                        '4) Алгоритм Брезенхема;\n'
                        '5) стандартым методом.\n'
                        '\nДля построения окружности необходимо задать центр (Xc, Yc)\n'
                        'и радиус R и выбрать метод построения из списка предложенных.\n'
                        '\nДля построения эллипса необходимо задать центр (Xc, Yc)\n'
                        'и радиусы Rx и Ry; выбрать метод построения из списка предложенных.\n'
                        '\nДля построения спектра фигур\n'
                        'необходимо задать центр фигуры, радиус(ы)\n'
                        'выбрать метод для построения,\n'
                        'а также шаг изменения и количество фигур.\n'
                        '\nДля анализа времени работы построения окружности нужно нажать на кнопку "Сравнение времени построение окружности".\n'
                        '\nДля анализа времени работы построения эллипса нужно нажать на кнопку "Сравнение времени построение эллипса".\n'
                        )

    clearCanvasBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран",
                               font=("Consoles", FONT_BUTTON), command=clear_screen)
    infoBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка",
                        font=("Consoles", FONT_BUTTON), command=show_info)

    clearCanvasBtn.place(x=20, y=start_column * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    infoBtn.place(x=20, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
