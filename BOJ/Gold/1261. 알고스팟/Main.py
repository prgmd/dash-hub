import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
dq = deque()

dq.append((0, 0))
dist[0][0] = 0

while dq:
    x, y = dq.popleft()

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < m and 0 <= ny < n and dist[ny][nx] == -1:
            if graph[ny][nx] == 0:
                dist[ny][nx] = dist[y][x]
                dq.appendleft((nx, ny))
            else:
                dist[ny][nx] = dist[y][x] + 1
                dq.append((nx, ny))

print(dist[n-1][m-1])