def DDA(x1, y1, x2, y2, colour="black", stepmode=False):
    point_list = []
    steps = 0
    if x1==x2 and y1==y2:
        point_list.append([round(x1), round(y1), colour])
    else:
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx >= dy:
            length = dx
        else:
            length = dy
        
        dx = (x2 - x1) / length
        dy = (y2 - y1) / length

        x = x1
        y = y1

        for i in range(0, int(length) + 1):
            if not stepmode:
                point_list.append([round(x), round(y), colour])
            elif round(x + dx) != round(x) and round(y + dy) != round(y):
                steps+=1
            x+=dx
            y+=dy

    if stepmode:
        return steps
    return point_list