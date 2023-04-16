MAIN_COLOUR = "#2b2b2b"
MAIN_FRAME_COLOUR = "#313335"
ADD_COLOUR = "#3c3f41"
TEXT_ENTRY_COLOUR = "#eeeeee"

FIGURE_FILE = "figure.txt"

WINDOW_W = 1900
WINDOW_H = 900

BORDERS_PART = 0.05
BORDERS_SPACE = 10
BORDERS_MAIN_MAKE = 1/6
COLUMNS_DATA_BORDERS_H = 1/5

DATA_PART_W = 0.28 - 2 * BORDERS_PART
DATA_PART_H = 0.8 - 2 * BORDERS_PART
DATA_K_LABEL = 1 - BORDERS_MAIN_MAKE
DATA_W = int(WINDOW_W * BORDERS_MAIN_MAKE)
DATA_H = int(WINDOW_H - BORDERS_SPACE * 2)

FIELD_W = WINDOW_W * (1 - BORDERS_MAIN_MAKE) - 3 * BORDERS_SPACE
FIELD_H = WINDOW_H - 2 * BORDERS_SPACE
CONST_FIELD_W = FIELD_W / 4 / 26
CONST_FIELD_H = FIELD_H / 2 / 33

POINT_SIZE = 6
LINE_WIDTH = 2

SCALE = 100
STEP = 1 * 10 / SCALE
INCLINE = 1
MAX_LIMIT_X = (FIELD_W / SCALE) // 2
MAX_LIMIT_Y = (FIELD_H / SCALE) // 2
MIN_LIMIT_X = -MAX_LIMIT_X
MIN_LIMIT_Y = -MAX_LIMIT_Y

COLUMNS = 23

INFO_PART_HEIGHT = (1 - DATA_PART_H - 2 * BORDERS_PART) - 1 * BORDERS_PART
INFO_PART_WIDTH = DATA_PART_W
INFO_WIDTH = int(INFO_PART_WIDTH * WINDOW_W)
INFO_HEIGHT = int(INFO_PART_HEIGHT * WINDOW_H)
INFO_COLS = 4