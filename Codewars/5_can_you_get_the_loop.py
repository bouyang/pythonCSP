def loop_size(node):
    seen = {}
    i = 0
    current = node

    while seen.get(current.next) == None:
        i += 1
        seen[current] = i
        current = current.next

    if i == seen.get(current.next): return 1

    return(i - seen.get(current.next) + 2)