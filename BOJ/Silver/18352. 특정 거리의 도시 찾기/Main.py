from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [1e9] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijk(start):
    q = deque()
    q.append((start, 0))
    dist[start] = 0

    while q:
        now, curr_dist = q.popleft()
        for nxt in graph[now]:
            if curr_dist < dist[nxt]:
                dist[nxt] = curr_dist+1
                q.append((nxt, curr_dist+1))

dijk(x)

answer = []
for i, v in enumerate(dist):
    if v == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)