import math

def find_next_square(sq):
    if sq % math.sqrt(sq) != 0:
        return -1
    
    while True:
        sq += 1
        if sq % math.sqrt(sq) == 0:
            return sq

print (121 % math.sqrt(121))