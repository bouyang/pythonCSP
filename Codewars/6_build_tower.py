def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors + 1):
        result.append((' ' * (n_floors - i)) + ('*' * (i * 2 - 1)) + (' ' * (n_floors - i)))

    return result

# 1 => 1
# 2 => 3
# 3 => 5
# 4 => 7

print(tower_builder(2))