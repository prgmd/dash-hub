sudoku = []
blank = []
for i in range(9):
    sudoku.append(list(map(int, input())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

def can_sudoku(y, x, k):
    for i in range(9):
        if (i != x and sudoku[y][i] == k) or (i != y and sudoku[i][x] == k):
            return False
    for i in range(3):
        for j in range(3):
            if sudoku[(y//3)*3+i][(x//3)*3+j] == k:
                return False
    return True

def bt(n):
    for i in range(n, len(blank)):
        y, x = blank[i]
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