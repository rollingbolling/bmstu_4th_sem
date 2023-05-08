import tkinter as tk
from tkinter import colorchooser, messagebox

from config import *

def place_draw_method(frame, methodDraw, start_column):
    modeMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="РЕЖИМ ЗАКРАСКИ",
                            font=("Consolas", 16),
                            fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    methodDraw.set(1)
    modeMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    tk.Radiobutton(frame, variable=methodDraw, text="С задержкой", value=0, bg=FRAME_COLOUR,
                    font=("Consolas", 16), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="white",
                    activebackground=FRAME_COLOUR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
                ).place(x=10, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 2 * BORDERS_SPACE,
                        height=FRAME_H // COLUMNS)
    tk.Radiobutton(frame, variable=methodDraw, text="Без задержки", value=1, bg=FRAME_COLOUR,
                    font=("Consolas", 16), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="white",
                    activebackground=FRAME_COLOUR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
                ).place(x=FRAME_W // 2, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 2 * BORDERS_SPACE,
                        height=FRAME_H // COLUMNS)
    

def place_clear_info_block(frame, clear_screen, start_column):
    def show_info():
        messagebox.showinfo("Info", 
                            "С помощью этой программы можно построить фигуру и закрасить её.\n"
                            "Для построения закраски используется алгоритм с упорядоченным списком ребер\n"
                            "и его реализация САР")

    clearCanvasBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран",
                               font=("Consoles", FONT_BUTTON), command=clear_screen)
    infoBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка",
                        font=("Consoles", FONT_BUTTON), command=show_info)

    clearCanvasBtn.place(x=20, y=start_column * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)
    infoBtn.place(x=20, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W - 40, height=FRAME_H // COLUMNS)


def place_draw_point(frame, xEntry, yEntry, listPoint_scroll, get_point, close_figure, start_column):
    pointMakeLabel = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ точки",
                            font=("Consolas", FONT_HEAD),
                            fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    msgAboutPoint = tk.Label(frame, bg=FRAME_COLOUR, text=("X{0}Y".format(" " * int(FRAME_W // 5.5 // FONT_LABEL))),
                            font=("Consolas", FONT_LABEL),
                            fg=MAIN_COLOUR_LABEL_TEXT)

    drawPointBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить точку", font=("Consolas", FONT_BUTTON),
                            command=get_point)
    drawCloseBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Замкнуть фигуру", font=("Consolas", FONT_BUTTON),
                            command=close_figure)

    pointMakeLabel.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    msgAboutPoint.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    xEntry.place(x=FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)
    yEntry.place(x=2 * FRAME_W // 4, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 4, height=FRAME_H // COLUMNS)

    drawPointBtn.place(x=10, y=(start_column + 3.5) * FRAME_H // COLUMNS, width=FRAME_W // 2, height=FRAME_H // COLUMNS)
    drawCloseBtn.place(x=FRAME_W // 2, y=(start_column + 3.5) * FRAME_H // COLUMNS, width=FRAME_W // 2 - 10, height=FRAME_H // COLUMNS)

    listPoint_scroll.place(x=40, y=(start_column + 5) * FRAME_H // COLUMNS, width=FRAME_W - 60, height=6 * FRAME_H // COLUMNS)


def place_mouse_mode(frame, fillingBtn, timeLabel, start_column):
    modeByMouse = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ с помощью мыши",
                                font=("Consolas", 16),
                                fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    labelTextInfo_1 = tk.Label(frame, bg=FRAME_COLOUR, text="Левая кнопка - добавить точку",
                                font=("Consolas", 14),
                                fg=MAIN_COLOUR_LABEL_TEXT)
    labelTextInfo_2 = tk.Label(frame, bg=FRAME_COLOUR, text="Правая кнопка - замкнуть фигуру",
                                font=("Consolas", 14),
                                fg=MAIN_COLOUR_LABEL_TEXT)
    
    modeByMouse.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    labelTextInfo_1.place(x=0, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    labelTextInfo_2.place(x=0, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)
    fillingBtn.place(x=40, y=(start_column + 3) * FRAME_H // COLUMNS, width=FRAME_W - 80, height=FRAME_H // COLUMNS)
    timeLabel.place(x=FRAME_W + 2 * BORDERS_SPACE, y=CANVAS_H + BORDERS_SPACE - FRAME_H // COLUMNS, width=FRAME_W - 60, height=FRAME_H // COLUMNS)
