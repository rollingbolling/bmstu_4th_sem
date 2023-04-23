# import numpy as np
import tkinter as tk
from tkinter import colorchooser, messagebox

import config as cfg


root = tk.Tk()
root.title("Lab №3")
root.geometry(str(cfg.WINDOW_W) + "x" + str(cfg.WINDOW_H))
root["bg"] = cfg.MAIN_COLOUR
root.resizable(False, False)


if __name__ == "__main__":
    # INPUT DATA FRAME


    dataFrame = tk.Frame(root)
    dataFrame["bg"] = cfg.FRAME_COLOUR

    dataFrame.place(x=cfg.BORDERS_SPACE, y=cfg.BORDERS_SPACE,
                    width=cfg.FRAME_W,
                    height=cfg.FRAME_H)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Кнопки для выбора алгоритма

    algorithmsLabel = tk.Label(dataFrame, bg=cfg.MAIN_COLOUR_LABEL_BG, text="АЛГОРИТМЫ ПОСТРОЕНИЯ",
                        font=("Consolas", 16),
                        fg=cfg.MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    algorithmsArr = [("Цифровой дифференциальный анализатор", 0),
                    ("Брензенхем (float)", 1),
                    ("Брензенхем (integer)", 2),
                    ("Брензенхем (c устр. ступенчатости)", 3),
                    ("By", 4),
                    ("Библиотечная функция", 5)]
    algorithmsRB = tk.IntVar()

    for value in range(len(algorithmsArr)):
        tk.Radiobutton(dataFrame, variable=algorithmsRB, text=algorithmsArr[value][0], value=value, bg=str(cfg.MAIN_COLOUR_BUTON_BG),
                    indicatoron=False, font=("Consolas", 16), justify=tk.LEFT, highlightbackground="black",
                    ).place(x=10, y=(value + 1) * cfg.FRAME_H // cfg.COLUMNS, width=cfg.FRAME_W - 2 * cfg.BORDERS_SPACE, height=cfg.FRAME_H // cfg.COLUMNS)

    algorithmsLabel .place(x=0, y=0, width=cfg.FRAME_W, height=cfg.FRAME_H // cfg.COLUMNS)


root.mainloop()