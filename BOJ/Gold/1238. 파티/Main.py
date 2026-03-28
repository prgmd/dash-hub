import sys
import heapq
n, m, x = map(int, input().split())
input = sys.stdin.readline

roads = {}
for _ in range(m):
    start, end, time = map(int, input().split())
    if start not in roads:
        roads[start] = []
    heapq.heappush(roads[start], (time, end))

go_costs = [1e9 for _ in range(n+1)]
back_costs = [1e9 for _ in range(n+1)]

for i in range(1, n+1):
    if i == x:
        go_costs[i] = 0
        continue

    temp_costs = [1e9 for _ in range(n+1)]
    temp_costs[i] = 0

    q = [i]
    while q:
        now = heapq.heappop(q)
        for dist, nxt in roads[now]:
            if temp_costs[nxt] > temp_costs[now] + dist:
                temp_costs[nxt] = temp_costs[now] + dist
                if nxt == x:
                    continue
                heapq.heappush(q, nxt)
                
    go_costs[i] = temp_costs[x]

q = [x]
back_costs[x] = 0

while q:
    now = heapq.heappop(q)
    for dist, nxt in roads[now]:
        if back_costs[nxt] > back_costs[now] + dist:
            back_costs[nxt] = back_costs[now] + dist
            heapq.heappush(q, nxt)

ans = 0
for i in range(1, n+1):
    ans = max(ans, go_costs[i] + back_costs[i])
print(ans)