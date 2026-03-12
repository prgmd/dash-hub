import sys
input = sys.stdin.readline

def solve():
    for t in range(int(input())):
        n, k = map(int, input().split())
        times = [0] + list(map(int, input().split()))
        builds = [[] for _ in range(n+1)]
        degree = [0]*(n+1)
        dp = [0]*(n+1)

        for _ in range(k):
            x, y = map(int, input().split())
            builds[x].append(y)
            degree[y] += 1


        w = int(input())

        q = []
        ptr = 0
        for idx, d in enumerate(degree):
            if not idx:
                continue
            if not d:
                q.append((idx, 1))
                dp[idx] += times[idx]
        size = len(q)

        while ptr < size:
            now, cnt = q[ptr]
            ptr += 1
            
            for nxt in builds[now]:
                degree[nxt] -= 1
                if not degree[nxt]:
                    q.append((nxt, cnt+1))                
                    size += 1
                dp[nxt] = max(times[nxt] + dp[now], dp[nxt])

        print(dp[w])

solve()