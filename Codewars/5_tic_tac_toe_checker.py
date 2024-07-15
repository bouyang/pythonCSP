def is_solved(board):
    for row in board:
        if row.count(1) == 3:
            return 1
        elif row.count(2) == 3:
            return 2

    for col in range(3):
        x = 0
        o = 0
        for row in range(3):
            if board[row][col] == 1:
                x += 1
            elif board[row][col] == 2:
                o += 1
        if x == 3:
            return 1
        elif o == 3:
            return 2
        
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1
    if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2
    
    zeroes = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                zeroes += 1
    if zeroes == 0:
        return 0
    
    return -1


board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]

board2 = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]

print(is_solved(board))
print(is_solved(board2))