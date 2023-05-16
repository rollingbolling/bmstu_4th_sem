from draw import *
import math as m

def parametric_circle(canvas, xc, yc, r, colour, draw):
    step = 1 / r
    i = 0
    while i < m.pi / 4 + step:
        x = xc + r * m.cos(i)
        y = yc + r * m.sin(i)
        if draw:
            draw_pixels(canvas, [xc, yc, colour], xc, yc, circle=True)
        i += step

def parametric_ellipse(canvas, xc, yc, ra, rb, colour, draw):
    if ra > rb:
        step = 1 / ra
    else:
        step = 1 / rb

    i = 0
    while i <= m.pi / 2 + step:
        x = xc + round(ra * m.cos(i))
        y = yc + round(rb * m.sin(i))

        if draw:
            draw_pixels(canvas, [x, y, colour], xc, yc, circle=False)

        i += step

