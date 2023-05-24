import tkinter as tk
from tkinter import colorchooser, messagebox

from config import *

def place_draw_method(frame, methodDraw, start_column):
    modeMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="РЕЖИМ ЗАКРАСКИ",
                            font=("Consolas", FONT_HEAD),
                            fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    methodDraw.set(1)
    modeMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    tk.Radiobutton(frame, variable=methodDraw, text="С задержкой", value=0, bg=FRAME_COLOUR,
                    font=("Consolas", FONT_LABEL), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="white",
                    activebackground=FRAME_COLOUR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
                ).place(x=10, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 2 * BORDERS_SPACE,
                        height=FRAME_H // COLUMNS)
    tk.Radiobutton(frame, variable=methodDraw, text="Без задержки", value=1, bg=FRAME_COLOUR,
                    font=("Consolas", FONT_LABEL), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="white",
                    activebackground=FRAME_COLOUR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
                ).place(x=FRAME_W // 2, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 2 * BORDERS_SPACE,
                        height=FRAME_H // COLUMNS)
    

def place_clear_info_block(frame, clear_screen, start_column):
    def show_info():
        messagebox.showinfo("Info", 
                            "С помощью этой программы можно построить фигуру и закрасить её.\n"
                            "Для построения закраски используется алгоритм затравки")

    clearCanvasBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран",
                               font=("Consoles", FONT_BUTTON), command=clear_screen)
    infoBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка",
                        font=("Consoles", FONT_BUTTON), command=show_info)

    clearCanvasBtn.place(x=20, y=start_column * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    infoBtn.place(x=20, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)


def place_draw_section(frame, xsEntry, ysEntry, xeEntry, yeEntry, draw_section, start_column):
    pointMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОТРЕЗКА",
                            font=("Consolas", FONT_HEAD),
                            fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    msgAboutPoint = tk.Label(frame, bg=FRAME_COLOUR, text=("Xн{0}Yн{0}Xк{0}Yк".format(" " * int(FRAME_W // 5.5 // FONT_LABEL))),
                            font=("Consolas", FONT_LABEL),
                            fg=MAIN_COLOUR_LABEL_TEXT)

    drawSectionBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить отрезок", font=("Consolas", FONT_BUTTON),
                            command=draw_section)

    pointMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    msgAboutPoint.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    xsEntry.place(x=0, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    ysEntry.place(x=FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    xeEntry.place(x=2 * FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    yeEntry.place(x=3 * FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)

    drawSectionBtn.place(x=FRAME_W // 4, y=(start_column + 3.5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    
def place_draw_cliper(frame, xclEntry, yclEntry, draw_cliper, close_cliper, start_column):
    pointMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОТСЕКАТЕЛЯ",
                            font=("Consolas", FONT_HEAD),
                            fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    msgAboutPoint = tk.Label(frame, bg=FRAME_COLOUR, text=("X{0}Y".format(" " * int(FRAME_W // 2.5 // FONT_LABEL))),
                            font=("Consolas", FONT_LABEL),
                            fg=MAIN_COLOUR_LABEL_TEXT)

    drawCliperBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить отсекатель", font=("Consolas", FONT_BUTTON),
                            command=draw_cliper)
    drawCloseCliperBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Замкнуть отсекатель", font=("Consolas", FONT_BUTTON),
                            command=close_cliper)

    pointMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    msgAboutPoint.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    xclEntry.place(x=0, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    yclEntry.place(x=FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

    drawCliperBtn.place(x=0, y=(start_column + 3.5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawCloseCliperBtn.place(x=FRAME_W // 2, y=(start_column + 3.5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)

def place_mouse_mode(frame, add_hor_vert_section, clip, start_column):
    modeByMouse = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ с помощью мыши",
                                font=("Consolas", FONT_HEAD),
                                fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    labelTextInfo_1 = tk.Label(frame, bg=FRAME_COLOUR, text="Левая кнопка - добавить отсекатель(Прямоугольник)",
                                font=("Consolas", FONT_LABEL),
                                fg=MAIN_COLOUR_LABEL_TEXT)
    labelTextInfo_2 = tk.Label(frame, bg=FRAME_COLOUR, text="Правая кнопка - добавить отрезок",
                                font=("Consolas", FONT_LABEL),
                                fg=MAIN_COLOUR_LABEL_TEXT)
    
    modeByMouse.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    labelTextInfo_1.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    labelTextInfo_2.place(x=0, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    addHorVertSectionBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Добавить горизонтальные \nи вертикальные отрезки", font=("Consolas", FONT_BUTTON),
                            command=add_hor_vert_section)
    clipBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Отсечь", font=("Consolas", FONT_BUTTON),
                            command=clip)
    addHorVertSectionBtn.place(x=FRAME_W // 4, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 20, height=2 * FRAME_H // COLUMNS)
    clipBtn.place(x=FRAME_W // 4, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 20, height=FRAME_H // COLUMNS)

    