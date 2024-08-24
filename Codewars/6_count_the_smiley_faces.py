import re

def count_smileys(arr):
    if len(arr) == 0: return 0

    regex = r'[:|;][-|~]?[)|D]'

    return len([ele for ele in arr if re.search(regex, ele) is not None])

print(count_smileys([':)', ';(', ';}', ':-D']))