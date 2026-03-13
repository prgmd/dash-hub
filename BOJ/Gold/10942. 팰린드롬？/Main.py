import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for y in range(n-1, -1, -1):
        for x in range(y+1, n):
            if board[y] != board[x]:
                continue

            if ((x-y) == 1 and dp[y+1][x] == 1) or (dp[y+1][x-1]):
                dp[y][x] = 1

    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])

solve()