def is_triangle(a, b, c):
    sides = sorted([a, b, c])
    return a > 0 and b > 0 and c > 0 and (sides[0] + sides[1] > sides[2])