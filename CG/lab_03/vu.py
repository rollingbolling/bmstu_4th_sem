from config import CANVAS_COLOUR
from methodfuncs import get_rgb_intens
from math import floor

def VU(canvas, x1, y1, x2, y2, fill="black", stepmode=False):
    point_list = []
    I = 100
    fills = get_rgb_intens(canvas, fill, CANVAS_COLOUR, I)
    if x1==x2 and y1==y2:
        point_list.append([x1, y1, fills[100]])
    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    xend = round(x1)
    yend = y1 + tg * (xend - x1)
    xpx1 = xend
    y = yend + tg

    xend = int(x2 + 0.5)
    xpx2 = xend

    steps = 0

    # main loop
    if steep:
        for x in range(xpx1, xpx2):
            try:
                point_list.append([int(y), x + 1, fills[int((I - 1) * (abs(1 - y + int(y))))]])
            except:
                point_list.append([int(y), x + 1, fill])
            point_list.append([int(y) + 1, x + 1, fills[int((I - 1) * (abs(y - int(y))))]])
            
            if x < round(x2) and int(y) != int(y + tg):
                steps += 1

            y += tg
    else:
        for x in range(xpx1, xpx2):
            point_list.append([x + 1, int(y), fills[round((I - 1) * (abs(1 - y + floor(y))))]])
            point_list.append([x + 1, int(y) + 1, fills[round((I - 1) * (abs(1 - y + floor(y))))]])

            if x < round(x2) and int(y) != int(y + tg):
                steps += 1

            y += tg
    if stepmode:
        return steps

    return point_list
