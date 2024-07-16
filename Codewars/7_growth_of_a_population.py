def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = int(p0 * (1 + (percent / 100)) + aug)
        years += 1
        print(p0)
    return years

print(nb_year(1000, 2.0, 50, 1214))