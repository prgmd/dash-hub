import sys
import heapq
n, m, x = map(int, input().split())
input = sys.stdin.readline

roads = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    heapq.heappush(roads[start], (time, end))

costs = [[1e9] * (n+1) for _ in range(n)]
ans = [0] * (n+1)

for i in range(1, n+1):
    row = costs[i-1]
    row[i] = 0

    q = [i]
    while q:
        now = heapq.heappop(q)
        for dist, nxt in roads[now]:
            if row[nxt] > row[now] + dist:
                row[nxt] = row[now] + dist
                if nxt == x:
                    continue
                heapq.heappush(q, nxt)

for i in range(1, n+1):
    if i == x:
        continue
    costs[x-1][i] += costs[i-1][x]

print(max(costs[x-1][1:]))