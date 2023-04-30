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


def place_line_colour_choice(frame, size_colour, start_column):
    def get_colour_circle():
        colour = colorchooser.askcolor(title="Choose colour circle")
        set_circle_colour(colour[-1])

    def set_circle_colour(colour):
        global LINE_COLOUR
        LINE_COLOUR = colour
        cur_colour_circle.configure(bg=LINE_COLOUR)

    cur_colour_text_label = tk.Label(frame, bg=FRAME_COLOUR, text="Текущий цвет окруж.:",
                                     font=("Consoles", FONT_LABEL),
                                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_circle = tk.Label(frame, bg="black")
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_circle = tk.Label(frame, bg=FRAME_COLOUR, text="Окруж.:", font=("Consoles", FONT_LABEL),
                             fg=MAIN_COLOUR_LABEL_TEXT)
    colour_circle.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)

    white_circle = tk.Button(frame, bg="white", activebackground="white",
                             command=lambda: set_circle_colour("white"))
    yellow_circle = tk.Button(frame, bg="yellow", activebackground="yellow",
                              command=lambda: set_circle_colour("yellow"))
    orange_circle = tk.Button(frame, bg="orange", activebackground="orange",
                              command=lambda: set_circle_colour("orange"))
    red_circle = tk.Button(frame, bg="red", activebackground="red", command=lambda: set_circle_colour("red"))
    purple_circle = tk.Button(frame, bg="purple", activebackground="purple",
                              command=lambda: set_circle_colour("purple"))
    light_green_circle = tk.Button(frame, bg="light green", activebackground="light green",
                                   command=lambda: set_circle_colour("light green"))
    green_circle = tk.Button(frame, bg="green", activebackground="green",
                             command=lambda: set_circle_colour("green"))
    light_blue_circle = tk.Button(frame, bg="light blue", activebackground="light blue",
                                  command=lambda: set_circle_colour("light blue"))

    white_circle.place(x=FRAME_W // 3 - BORDERS_SPACE, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    yellow_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    orange_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    red_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                     height=FRAME_H // COLUMNS)
    purple_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    light_green_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=start_column * FRAME_H // COLUMNS,
                             width=size_colour, height=FRAME_H // COLUMNS)
    green_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    light_blue_circle.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=start_column * FRAME_H // COLUMNS,
                            width=size_colour, height=FRAME_H // COLUMNS)

    circle_colour_change = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет CIRCLE",
                                     font=("Consoles", 11), command=get_colour_circle)
    circle_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                               height=FRAME_H // COLUMNS)


def place_algo_choose(frame, start_column):
    algorithms_label = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="АЛГОРИТМЫ ПОСТРОЕНИЯ",
                                font=("Consoles", FONT_HEAD),
                                fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    algorithms_arr = [("Каноническое уравнение", 0),
                      ("Параметрическое уравнение", 1),
                      ("Алгоритм средней точки", 2),
                      ("Алгоритм Брензенхема", 3),
                      ("Библиотечная функция", 4)]
    algorithms_rb = tk.IntVar()

    for value in range(len(algorithms_arr)):
        tk.Radiobutton(frame, variable=algorithms_rb, text=algorithms_arr[value][0], value=value,
                       bg=str(MAIN_COLOUR_BUTON_BG),
                       indicatoron=False, font=("Consoles", FONT_BUTTON), justify=tk.LEFT, highlightbackground="black",
                       ).place(x=10, y=(start_column + value + 1) * FRAME_H // COLUMNS, width=FRAME_W - 2 * BORDERS_SPACE,
                               height=FRAME_H // COLUMNS)

    algorithms_label.place(x=0, y=start_column, width=FRAME_W, height=FRAME_H // COLUMNS)


def place_colour_choose_block(frame, canvas, start_column):
    size_colour = (FRAME_W // 1.5) // 8

    colour_choice_label = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА", font=("Consoles", FONT_HEAD),
                                   fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    colour_choice_label.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    place_bg_colour_choice(frame, canvas, size_colour, start_column + 1)

    place_line_colour_choice(frame, size_colour, start_column + 3)


def place_draw_figure_block(frame, draw_circle, draw_ellipse, start_column):
    circleMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ФИГУРЫ",
                               font=("Consoles", FONT_HEAD),
                               fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    argumentsLabel = tk.Label(frame, bg=FRAME_COLOUR,
                              text=("X{0}Y".format(" " * int(FRAME_W // 1.5 // FONT_LABEL))),
                              font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT)

    xcEntry = tk.Entry(frame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                       justify="center")
    ycEntry = tk.Entry(frame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                       justify="center")
    drawCircleBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить окр.",
                              font=("Consoles", FONT_BUTTON), command=draw_circle)
    drawEllipseBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить эллипс",
                               font=("Consoles", FONT_BUTTON), command=draw_ellipse)

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

    circle_radEntry = tk.Entry(frame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    ellipse_wEntry = tk.Entry(frame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")
    ellipse_hEntry = tk.Entry(frame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")

    circle_radLabel.place(x=0, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    circle_radEntry.place(x=FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wLabel.place(x=2 * FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_wEntry.place(x=3 * FRAME_W // 4, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hLabel.place(x=2 * FRAME_W // 4, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ellipse_hEntry.place(x=3 * FRAME_W // 4, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)


def place_draw_spectre_block(dataFrame, draw_circle_spec, draw_ellipse_spec, start_column):
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

    circle_radEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    ellipse_wEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")
    ellipse_hEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")

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
    figureAmountEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                                 justify="center")
    figureStepEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    figureStepLabel.place(x=0, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureStepEntry.place(x=FRAME_W // 2, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureAmountLabel.place(x=0, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    figureAmountEntry.place(x=FRAME_W // 2, y=(start_column + 4) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

    drawSpecCircleBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр окр.",
                                  font=("Consoles", FONT_BUTTON), command=draw_circle_spec)
    drawSpecEllipseBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр элип.",
                                   font=("Consoles", FONT_BUTTON), command=draw_ellipse_spec)
    drawSpecCircleBtn.place(x=0, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawSpecEllipseBtn.place(x=FRAME_W // 2, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)


def place_analys_block(frame, time_analys_circle, time_analys_ellipse, start_column):
    StatsLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="АНАЛИЗ",
                          font=("Consolas", FONT_HEAD),
                          fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    compareCircleTimeBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Анализ времени",
                                     font=("Consolas", FONT_BUTTON),
                                     command=time_analys_circle)
    compareSpecTimeBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Анализ времени",
                                   font=("Consolas", FONT_BUTTON),
                                   command=time_analys_ellipse)

    StatsLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    compareCircleTimeBtn.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    compareSpecTimeBtn.place(x=FRAME_W // 2, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)


def place_clear_info_block(frame, clear_screen, start_column):
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

    clearCanvasBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран",
                               font=("Consoles", FONT_BUTTON), command=clear_screen)
    infoBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка",
                        font=("Consoles", FONT_BUTTON), command=show_info)

    clearCanvasBtn.place(x=20, y=start_column * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    infoBtn.place(x=20, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
