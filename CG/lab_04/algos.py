from brezenhem import brezenhem_circle, brezenhem_ellipse

from canonic import canonic_circle, canonic_ellipse

from parametric import parametric_circle, parametric_ellipse

from midpoint import midpoint_circle, midpoint_ellipse


def stand_oval(canvas, xc, yc, ra, rb, colour):
    canvas.create_oval(xc-ra, yc-rb, xc+ra, yc+rb, outline=colour)

def spectrumBy_standart(canvas, xc, yc, ra, rb, step, count, colour):
    for e in range(0, count):
        stand_oval(canvas, xc, yc, ra, rb, colour)
        ra += step
        rb += step


def spectrumCircleBy_algorith(canvas, alg, xc, yc, rs, step, count, colour):
    for e in range(0, count):
        alg(canvas, xc, yc, rs, colour, True)
        rs += step


def spectrumEllipseBy_algorith(canvas, alg, xc, yc, ra, rb, step, count, colour):
    constant = ra / rb
    for e in range(0, count):
        alg(canvas, xc, yc, ra, rb, colour, True)
        ra += step
        rb = round(ra / constant)

def add_ellipse(canvas, algorithm, xc, yc, ra, rb, colour, drawMode=True):
    try:
        alg = algorithm.get()

    except AttributeError:
        alg = algorithm

    if alg == 0:
        canonic_ellipse(canvas, xc, yc, ra, rb, colour, drawMode)
    elif alg == 1:
        parametric_ellipse(canvas, xc, yc, ra, rb, colour, drawMode)
    elif alg == 2:
        midpoint_ellipse(canvas, xc, yc, ra, rb, colour, drawMode)
    elif alg == 3:
        brezenhem_ellipse(canvas, xc, yc, ra, rb, colour, drawMode)
    else:
        stand_oval(canvas, xc, yc, ra, rb, colour)
        return


def add_circle(canvas, algorithm, xc, yc, r, colour, drawMode=True):
    try:
        alg = algorithm.get()

    except:
        alg = algorithm
    
    if alg == 0:
        canonic_circle(canvas, xc, yc, r, colour, drawMode)
    elif alg == 1:
        parametric_circle(canvas, xc, yc, r, colour, drawMode)
    elif alg == 2:
        midpoint_circle(canvas, xc, yc, r, colour, drawMode)
    elif alg == 3:
        brezenhem_circle(canvas, xc, yc, r, colour, drawMode)
    else:
        stand_oval(canvas, xc, yc, r, r, colour)
        return
