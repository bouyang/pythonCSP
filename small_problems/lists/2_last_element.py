def last(list):
    if list:
        return list[len(list) - 1]
    else:
        return None
    
print(last(['Earth', 'Moon', 'Mars']))  # Mars