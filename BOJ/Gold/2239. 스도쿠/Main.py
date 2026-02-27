sudoku = [list(map(int, input())) for _ in range(9)]

def can_sudoku(y, x, k):
    for i in range(9):
        if i != x and sudoku[y][i] == k:
            return False
        if i != y and sudoku[i][x] == k:
            return False
    for i in range((y//3)*3, (y//3)*3+3):
        for j in range((x//3)*3, (x//3)*3+3):
            if sudoku[i][j] == k:
                return False
    return True

def bt(n):
    for i in range(n, 81):
        y, x = i//9, i%9
        if sudoku[y][x] == 0:
            for j in range(1, 10):
                if can_sudoku(y, x, j):
                    sudoku[y][x] = j
                    bt(n+1)
                    sudoku[y][x] = 0
            else:
                return

    for s in sudoku:
        print(''.join(map(str, s)))
    exit()
                    
bt(0)