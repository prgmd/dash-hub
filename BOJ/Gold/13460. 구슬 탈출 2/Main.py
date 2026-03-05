from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 공의 위치
for y in range(1, n-1):
    for x in range(1, m-1):
        if board[y][x] != '.':
            if board[y][x] == 'B':
                by, bx = y, x
            if board[y][x] == 'R':
                ry, rx = y, x

# 공 움직이기
def bfs(ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0))
    visited = set()
    visited.add((ry, rx, by, bx))

    while q:
        ry, rx, by, bx, move = q.popleft()

        if move >= 10:
            return -1

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nry, nrx = ry, rx
            red_move = 0        
            while board[nry+dy][nrx+dx] != '#' and board[nry+dy][nrx+dx] != 'O':
                nry += dy
                nrx += dx
                red_move += 1
            
            nby, nbx = by, bx
            blue_move = 0
            while board[nby+dy][nbx+dx] != '#' and board[nby+dy][nbx+dx] != 'O':
                nby += dy
                nbx += dx
                blue_move += 1

            if board[nby+dy][nbx+dx] == 'O':
                continue

            if board[nry+dy][nrx+dx] == 'O':
                return move+1

            if (nry, nrx) == (nby, nbx):
                if red_move > blue_move:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            if (nry, nrx, nby, nbx) not in visited:
                visited.add((nry, nrx, nby, nbx))
                q.append((nry, nrx, nby, nbx, move+1))
    
    return -1

ans = bfs(ry, rx, by, bx)
print(ans)