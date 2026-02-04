from collections import defaultdict
import heapq

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = defaultdict(list)
answer = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

for item in range(1, len(items)):
    dist = [int(1e9)] * (n + 1)
    dist[item] = 0
    
    q = [(m, item)]
    while q:
        left_dist, now = heapq.heappop(q)
        
        if left_dist < 0:
            continue

        for nxt_dist, nxt in graph[now]:
            if nxt_dist <= left_dist:
                heapq.heappush(q, (left_dist-nxt_dist, nxt))
                dist[nxt] = min(dist[nxt], left_dist-nxt_dist)
        
    # answer와 값 비교
    item_total = 0
    for idx, d in enumerate(dist):
        if d <= m:
            item_total += items[idx]
    answer = max(item_total, answer)
    
print(answer)