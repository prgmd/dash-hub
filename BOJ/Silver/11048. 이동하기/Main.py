import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for y in range(n):
    for x in range(m):
        temp_max = 0
        for dy, dx in [(0, -1), (-1, 0), (-1, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                temp_max = max(dp[ny][nx], temp_max)
        dp[y][x] = temp_max + candy[y][x]

print(dp[n-1][m-1])