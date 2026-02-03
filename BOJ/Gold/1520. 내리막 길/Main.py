import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x):
    if (y, x) == (n-1, m-1):
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and graph[y][x] > graph[ny][nx]:    
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]

dfs(0, 0)
print(dp[0][0])