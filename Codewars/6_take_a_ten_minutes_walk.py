def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') != walk.count('s') or walk.count('e') != walk.count('w'):
        return False
    return True