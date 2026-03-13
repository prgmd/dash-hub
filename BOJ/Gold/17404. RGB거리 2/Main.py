import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e9)] * 3 for _ in range(n)]
ans = int(1e9)

def fill_dp(start):
    global ans
    
    if start == 0:
        dp[0] = [rgb[0][0], int(1e9), int(1e9)]
    elif start == 1:
        dp[0] = [int(1e9), rgb[0][1], int(1e9)]
    else:
        dp[0] = [int(1e9), int(1e9), rgb[0][2]]
    
    for y in range(1, n):
        if y == n-1:
            if start != 0:
                dp[y][0] = rgb[y][0] + min(dp[y-1][1], dp[y-1][2])
            if start != 1:
                dp[y][1] = rgb[y][1] + min(dp[y-1][0], dp[y-1][2])
            if start != 2:
                dp[y][2] = rgb[y][2] + min(dp[y-1][0], dp[y-1][1])
            ans = min(ans, min(dp[-1]))
        else:
            dp[y][0] = rgb[y][0] + min(dp[y-1][1], dp[y-1][2])
            dp[y][1] = rgb[y][1] + min(dp[y-1][0], dp[y-1][2])
            dp[y][2] = rgb[y][2] + min(dp[y-1][0], dp[y-1][1])

for x in range(3):
    fill_dp(x)

print(ans)