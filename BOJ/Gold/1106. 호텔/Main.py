import sys
input = sys.stdin.readline

def solve():
    c, n = map(int, input().split())
    hotel = []
    for _ in range(n):
        cost, customer = map(int, input().split())
        hotel.append((cost, customer))

    total = c+100
    dp = [int(1e9)] * (total)
    dp[0] = 0

    for cost, customer in hotel:
        for i in range(customer, total):
            dp[i] = min(dp[i-customer]+cost, dp[i])

    ans = min(dp[c:])
    print(ans)

solve()