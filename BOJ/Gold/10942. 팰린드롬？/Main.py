import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    def is_pellin(x1, x2):
        if board[x1:x2+1] == board[x1:x2+1][::-1]:
            return True
        return False

    for y in range(n-1):
        for x in range(y+1, n):
            if y != 0 and x != n-1:
                continue
            if is_pellin(y, x):
                i, j = y, x
                while i < j:
                    dp[i][j] = 1
                    i += 1
                    j -= 1

    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])

solve()