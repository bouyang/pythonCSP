def is_merge(s, part1, part2):

    part1 = list(part1)
    part2 = list(part2)
    bank = []

    for letter in list(s):
        if len(part1) > 0 and len(part2) > 0 and letter == part1[0] and letter == part2[0]:
            bank.append(part1[0])
            part1.pop(0)
            part2.pop(0)
        elif len(part1) > 0 and letter == part1[0]:
            part1.pop(0)
        elif len(part2) > 0 and letter == part2[0]:
            part2.pop(0)
        elif len(bank) > 0 and bank.count(letter) >= 1:
            bank.remove(letter)
        else:
            
            return False
            
    return len(part1) == 0 and len(part2) == 0 and len(bank) == 0


print(is_merge('DxyXRCDxyDVq;P;', 'DxyDVqP;', 'DxyXRC;'))