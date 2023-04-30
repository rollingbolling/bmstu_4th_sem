from screeninfo import get_monitors

MAIN_COLOUR = "#393A3A"
FRAME_COLOUR = "#575959"
CANVAS_COLOUR = "#F4F4F4"
LINE_COLOUR = "black"

MAIN_COLOUR_LABEL_BG = "#FF642F"
MAIN_COLOUR_LABEL_TEXT = "black"
MAIN_COLOUR_BUTON_BG = "#F89344"

monitor = get_monitors()
WINDOW_W = monitor[0].width
WINDOW_H = int(monitor[0].height * 9/10)

FONT_HEAD = 16
FONT_BUTTON = 10
FONT_ENTRY = 12
FONT_LABEL = 12

FRAME_SITUATION = 1/4
BORDERS_SPACE = 10

FRAME_W = WINDOW_W * FRAME_SITUATION - BORDERS_SPACE
FRAME_H = WINDOW_H - 2 * BORDERS_SPACE

CANVAS_SITUATION = 1 - FRAME_SITUATION
COLUMNS = 34

CANVAS_H = WINDOW_H - 2 * BORDERS_SPACE
CANVAS_W = WINDOW_W * CANVAS_SITUATION - 2 * BORDERS_SPACE

PLOT_W = WINDOW_W // 160
PLOT_H = WINDOW_H // 160
