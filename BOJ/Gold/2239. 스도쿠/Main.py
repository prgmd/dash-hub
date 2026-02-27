sudoku = []
blank = []

row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

for y in range(9):
    sudoku.append(list(map(int, input())))
    for x in range(9):
        now = sudoku[y][x]
        if now == 0:
            blank.append((y, x))
        else:
            row_check[y][now] = True
            col_check[x][now] = True
            box_check[(y//3)*3 + (x//3)][now] = True

def bt(n):
    if n == len(blank):
        for s in sudoku:
            print(''.join(map(str, s)))
        exit()

    for i in range(n, len(blank)):
        y, x = blank[i]
        box_idx = (y//3)*3 + (x//3)
        for j in range(1, 10):
            if not row_check[y][j] and not col_check[x][j] and not box_check[box_idx][j]:
                sudoku[y][x] = j
                row_check[y][j] = col_check[x][j] = box_check[box_idx][j] = True
                bt(n+1)
                sudoku[y][x] = 0
                row_check[y][j] = col_check[x][j] = box_check[box_idx][j] = False               
        else:
            return 
                           
bt(0)