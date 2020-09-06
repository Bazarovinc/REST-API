import math as m


def condition(x0, y0, x1, y1, r):
    if m.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2)) <= r:
        return True
    return False