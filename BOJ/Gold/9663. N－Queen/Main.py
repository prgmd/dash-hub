n = int(input())
answer = 0
board = [-1 for _ in range(n)]

def is_safe(y, x):
    if y == 0:
        return True
    
    for i in range(y):
        if board[i] == x or abs(y - i) == abs(x - board[i]):
            return False
    return True

def bt(y):
    global answer

    if y == n:
        answer += 1
        return

    for x in range(n):
        if is_safe(y, x):
            board[y] = x
            bt(y+1)

bt(0)
print(answer)