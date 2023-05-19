from ui import *
from algos import *
from time_measure import time_comparison

# BUTTON_FUNCS
def draw_circle():
    xc = xcEntry.get()
    yc = ycEntry.get()
    r = circle_radEntry.get()

    if not xc or not yc:
        messagebox.showwarning("ERROR", "Center not entered")
    elif not r:
        messagebox.showwarning("ERROR", "Radius not entered")
    else:
        try:
            xc = int(xc)
            yc = int(yc)
        except ValueError():
            messagebox.showwarning("ERROR", "Incorect input of center coords")
        try:
            r = int(r)
            if r <= 0:
                messagebox.showwarning("ERROR", "Incorect value of radius")
        except ValueError():
            messagebox.showwarning("ERROR", "Incorect radius input")
        add_circle(canvasField, algorithms_rb, xc, yc, r, LINE_COLOUR)

def draw_ellipse():
    xc = xcEntry.get()
    yc = ycEntry.get()
    ra = ellipse_wEntry.get()
    rb = ellipse_hEntry.get()

    if not xc or not yc:
        messagebox.showwarning("ERROR", "Center not entered")
    elif not ra:
        messagebox.showwarning("ERROR", "Width not entered")
    elif not rb:
        messagebox.showwarning("ERROR", "Height not entered")
    else:
        try:
            xc = int(xc)
            yc = int(yc)
        except ValueError():
            messagebox.showwarning("ERROR", "Incorect input of center coords")
        try:
            ra = int(ra)
            rb = int(rb)
            if ra <= 0 or rb <= 0:
                messagebox.showwarning("ERROR", "Incorect value of width or height")
        except ValueError():
            messagebox.showwarning("ERROR", "Incorect width or height input")
        add_ellipse(canvasField, algorithms_rb, xc, yc, ra, rb, LINE_COLOUR)

def draw_spectrum(mode):

    xc = xcEntry.get()
    yc = ycEntry.get()

    if not xc or not yc:
        messagebox.showwarning('Ошибка ввода',
                               'Не заданы координаты центра фигуры!')
    else:
        try:
            xc = int(xc)
            yc = int(yc)
        except ValueError:
            messagebox.showwarning("Ошибка",
                                   "Неверно заданы координаты центра (Xc, Yc) фигуры!\n"
                                   "Ожидался ввод целых чисел.")
            return

        step = figurespecStepEntry.get()
        count = figurespecAmountEntry.get()
        if not step:
            messagebox.showwarning('Ошибка ввода',
                                   'Не задан шаг изменения!')
        elif not count:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданo количество фигур!')
        else:
            try:
                step = int(step)
                if step <= 0:
                    messagebox.showwarning("Ошибка",
                                           "Неверно заданы шаг изменения фигуры не может быть меньше 1 при построении спектра!\n")
                    return
            except ValueError:
                messagebox.showwarning("Ошибка",
                                       "Неверно заданы шаг изменения фигуры при построении спектра!\n"
                                       "Ожидался ввод целых чисел.")
                return
            try:
                count = int(count)
                if count <= 0:
                    messagebox.showwarning("Ошибка",
                                           "Неверно заданы кол-во фигур не может быть меньше 1 при построении спектра!\n")
                    return
            except ValueError:
                messagebox.showwarning("Ошибка",
                                       "Неверно заданы кол-во фигур при построении спектра!\n"
                                       "Ожидался ввод целых чисел.")
                return
            if mode == "circle":

                rs = circlespec_radEntry.get()
                if not rs:
                    messagebox.showwarning('Ошибка ввода',
                                           'Не заданo начальный радиус окружности для построения спектра!')
                else:
                    try:
                        rs = int(rs)
                        if rs <= 0:
                            messagebox.showwarning("Ошибка",
                                                   "Неверно задан начальный радиус окружности не может быть меньше 1 для построения спектра!\n")
                            return
                    except ValueError:
                        messagebox.showwarning("Ошибка",
                                               "Неверно задан начальный радиус окружности для построения спектра!\n"
                                               "Ожидался ввод целого числа.")
                        return

                    value_alg = algorithms_rb.get()
                    if value_alg == 0:
                        spectrumCircleBy_algorith(canvasField, canonic_circle, xc, yc, rs, step, count, LINE_COLOUR)
                    elif value_alg == 1:
                        spectrumCircleBy_algorith(canvasField, parametric_circle, xc, yc, rs, step, count, LINE_COLOUR)
                    elif value_alg == 2:
                        spectrumCircleBy_algorith(canvasField, midpoint_circle, xc, yc, rs, step, count, LINE_COLOUR)
                    elif value_alg == 3:
                        spectrumCircleBy_algorith(canvasField, brezenhem_circle, xc, yc, rs, step, count, LINE_COLOUR)
                    elif value_alg == 4:
                        spectrumBy_standart(canvasField, xc, yc, rs, rs, step, count, LINE_COLOUR)
            elif mode == "ellipse":
                ra = ellipsespec_wEntry.get()
                rb = ellipsespec_hEntry.get()
                if not ra or not rb:
                    messagebox.showwarning('Ошибка ввода',
                                           'Не заданo начальные радиусы эллипса для построения спектра!')
                else:
                    try:
                        ra = int(ra)
                        rb = int(rb)
                        if ra <= 0 or rb <= 0:
                            messagebox.showwarning("Ошибка",
                                                   "Неверно задан начальные радиусы эллипса не могут быть меньше 1 для построения спектра!\n")
                            return
                    except ValueError:
                        messagebox.showwarning("Ошибка",
                                               "Неверно задан начальные радиусы эллипса для построения спектра!\n"
                                               "Ожидался ввод целых чисел.")
                        return

                    value_alg = algorithms_rb.get()
                    if value_alg == 0:
                        spectrumEllipseBy_algorith(canvasField, canonic_ellipse, xc, yc, ra, rb, step, count, LINE_COLOUR)
                    elif value_alg == 1:
                        spectrumEllipseBy_algorith(canvasField, parametric_ellipse, xc, yc, ra, rb, step, count, LINE_COLOUR)
                    elif value_alg == 2:
                        spectrumEllipseBy_algorith(canvasField, midpoint_ellipse, xc, yc, ra, rb, step, count, LINE_COLOUR)
                    elif value_alg == 3:
                        spectrumEllipseBy_algorith(canvasField, brezenhem_ellipse, xc, yc, ra, rb, step, count, LINE_COLOUR)
                    elif value_alg == 4:
                        spectrumBy_standart(canvasField, xc, yc, ra, rb, step, count, LINE_COLOUR)

def draw_axes():
    colour = "gray"
    canvasField.create_line(0, 3, CANVAS_W, 3, width=1, fill='gray', arrow=tk.LAST)
    canvasField.create_line(3, 0, 3, CANVAS_H, width=1, fill='gray', arrow=tk.LAST)
    for i in range(50, int(CANVAS_W), 50):
        canvasField.create_text(i, 15, text=str(abs(i)), fill=colour)
        canvasField.create_line(i, 0, i, 5, fill=colour)
    for i in range(50, int(CANVAS_H), 50):
        canvasField.create_text(15, i, text=str(abs(i)), fill=colour)
        canvasField.create_line(0, i, 5, i, fill=colour)

def place_line_colour_choice(frame, size_colour, start_column):
    def get_colour_line():
        colour = colorchooser.askcolor(title="Choose colour line")
        set_line_colour(colour[-1])

    def set_line_colour(colour):
        global LINE_COLOUR
        LINE_COLOUR = colour
        cur_colour_line.configure(bg=LINE_COLOUR)

    cur_colour_text_label = tk.Label(frame, bg=FRAME_COLOUR, text="Текущий цвет LINE:",
                                     font=("Consoles", FONT_LABEL),
                                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_line = tk.Label(frame, bg="black")
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_line = tk.Label(frame, bg=FRAME_COLOUR, text="LINE:", font=("Consoles", FONT_LABEL),
                             fg=MAIN_COLOUR_LABEL_TEXT)
    colour_line.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)

    white_line = tk.Button(frame, bg="white", activebackground="white",
                             command=lambda: set_line_colour("white"))
    yellow_line = tk.Button(frame, bg="yellow", activebackground="yellow",
                              command=lambda: set_line_colour("yellow"))
    orange_line = tk.Button(frame, bg="orange", activebackground="orange",
                              command=lambda: set_line_colour("orange"))
    red_line = tk.Button(frame, bg="red", activebackground="red", command=lambda: set_line_colour("red"))
    purple_line = tk.Button(frame, bg="purple", activebackground="purple",
                              command=lambda: set_line_colour("purple"))
    light_green_line = tk.Button(frame, bg="light green", activebackground="light green",
                                   command=lambda: set_line_colour("light green"))
    green_line = tk.Button(frame, bg="green", activebackground="green",
                             command=lambda: set_line_colour("green"))
    light_blue_line = tk.Button(frame, bg="light blue", activebackground="light blue",
                                  command=lambda: set_line_colour("light blue"))

    white_line.place(x=FRAME_W // 3 - BORDERS_SPACE, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    yellow_line.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    orange_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    red_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                     height=FRAME_H // COLUMNS)
    purple_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    light_green_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=start_column * FRAME_H // COLUMNS,
                             width=size_colour, height=FRAME_H // COLUMNS)
    green_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    light_blue_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=start_column * FRAME_H // COLUMNS,
                            width=size_colour, height=FRAME_H // COLUMNS)

    line_colour_change = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет LINE",
                                     font=("Consoles", 11), command=get_colour_line)
    line_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                               height=FRAME_H // COLUMNS)

def clear_screen():
    canvasField.delete("all")
    draw_axes()


# LAB WINDOW CREATION + SIZE CONFIGURATION
root = tk.Tk()
root.title("Lab №3")
root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(True, True)

# UI
if __name__ == "__main__":
    # FRAME CREATION
    dataFrame = tk.Frame(root)
    dataFrame["bg"] = FRAME_COLOUR
    dataFrame.place(x=BORDERS_SPACE, y=BORDERS_SPACE, width=FRAME_W, height=FRAME_H)

    # CANVAS CREATION
    canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
    canvasField.place(x=WINDOW_W * FRAME_SITUATION + BORDERS_SPACE, y=BORDERS_SPACE, width=CANVAS_W, height=CANVAS_H)
    draw_axes()

    # ВЫБОР АЛГОРИТМА
    algorithms_rb = tk.IntVar()
    place_algo_choose(dataFrame, algorithms_rb, 0)

    # ВЫБОР ЦВЕТА
    size_colour = (FRAME_W // 1.5) // 8
    colour_choice_label = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА", font=("Consoles", FONT_HEAD),
                                   fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    colour_choice_label.place(x=0, y=7 * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    place_bg_colour_choice(dataFrame, canvasField, size_colour, 8)
    place_line_colour_choice(dataFrame, size_colour, 10)

    # DRAW FIGURE
    xcEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                       justify="center")
    ycEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                       justify="center")
    circle_radEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    ellipse_wEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")
    ellipse_hEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")

    drawCircleBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить окр.",
                              font=("Consoles", FONT_BUTTON), command=draw_circle)
    drawEllipseBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить эллипс",
                               font=("Consoles", FONT_BUTTON), command=draw_ellipse)

    place_draw_figure_block(dataFrame, xcEntry, ycEntry, circle_radEntry, ellipse_wEntry, ellipse_hEntry, drawCircleBtn, drawEllipseBtn, 14)

    # DRAW SPECTOR
    circlespec_radEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    ellipsespec_wEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")
    ellipsespec_hEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                              justify="center")
    figurespecAmountEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                                 justify="center")
    figurespecStepEntry = tk.Entry(dataFrame, bg=FRAME_COLOUR, font=("Consoles", FONT_LABEL), fg=MAIN_COLOUR_LABEL_TEXT,
                               justify="center")
    drawSpecCircleBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр окр.",
                                  font=("Consoles", FONT_BUTTON), command=lambda:draw_spectrum("circle"))
    drawSpecEllipseBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр элип.",
                                   font=("Consoles", FONT_BUTTON), command=lambda:draw_spectrum("ellipse"))
    place_draw_spectre_block(dataFrame, circlespec_radEntry, ellipsespec_hEntry, ellipsespec_wEntry, figurespecAmountEntry, figurespecStepEntry, drawSpecCircleBtn, drawSpecEllipseBtn, 22)

    # INFO & STATS
    compareCircleTimeBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Анализ времени cir.",
                                     font=("Consolas", FONT_BUTTON),
                                     command=lambda:time_comparison(canvasField, LINE_COLOUR, "circle"))
    compareSpecTimeBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Анализ времени el.",
                                   font=("Consolas", FONT_BUTTON),
                                   command=lambda:time_comparison(canvasField, LINE_COLOUR, "ellipse"))
    place_analys_block(dataFrame, compareCircleTimeBtn, compareSpecTimeBtn, 29)
    place_clear_info_block(dataFrame, clear_screen, 32)

root.mainloop()
