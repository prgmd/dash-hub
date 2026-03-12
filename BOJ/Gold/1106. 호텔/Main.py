import sys
input = sys.stdin.readline

def solve():
    c, n = map(int, input().split())
    hotel = []
    for _ in range(n):
        cost, customer = map(int, input().split())
        hotel.append((cost, customer))
    # hotel.sort(key=lambda x:(x[1]/x[0]), reverse=True)

    total = c+100
    dp = [int(1e9)] * (total)
    dp[0] = 0

    for i in range(1, total):
        for cost, customer in hotel:
            if customer <= i:
                dp[i] = min(dp[i], dp[i-customer]+cost)

    ans = int(1e9)
    for i in range(c, total):
        ans = min(ans, dp[i])

    print(ans)

solve()