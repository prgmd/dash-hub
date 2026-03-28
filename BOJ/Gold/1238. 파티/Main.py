import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
roads = [[] for _ in range(n+1)]
rev_roads = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    roads[start].append((time, end))
    rev_roads[end].append((time, start))

def dijkstra(start, graph):
    cost = [1e9] * (n+1)
    cost[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        if cost[now] < dist:
            continue

        for weight, nxt in graph[now]:
            if cost[nxt] > dist + weight:
                cost[nxt] = dist + weight
                heapq.heappush(q, (cost[nxt], nxt))
    
    return cost

go_party = dijkstra(x, roads)
go_home = dijkstra(x, rev_roads)
ans = 0

for i in range(1, n+1):
    if i == x:
        continue
    ans = max(ans, go_party[i] + go_home[i])
print(ans)