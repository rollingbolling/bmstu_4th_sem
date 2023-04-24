from math import cos, sin

def get_sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
    
def get_rgb_intens(canvas, colour, bg_colour, intens):
    grad = []
    (r1, g1, b1) = canvas.winfo_rgb(colour)
    (r2, g2, b2) = canvas.winfo_rgb(bg_colour)
    r_ratio = float(r2 - r1) / intens
    g_ratio = float(g2 - g1) / intens
    b_ratio = float(b2 - b1) / intens
    for i in range(intens):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        grad.append("#%4.4x%4.4x%4.4x" % (nr, ng, nb))
    grad.reverse
    return grad

def turn_point(angle, px, py, cx, cy):
    x = px
    px = round(cx + (x - cx) * cos(angle) + (py - cy) * sin(angle))
    py = round(cy - (x - cx) * sin(angle) + (py - cy) * cos(angle))
    return px, py