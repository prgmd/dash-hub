from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input() for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

white_power, blue_power = 0, 0

def bfs(y, x):
    global white_power
    global blue_power

    q = deque()
    q.append((y, x))
    color = graph[y][x]
    visited[y][x] = 1
    cnt = 0

    while q:
        cnt += 1
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] == 0:
                for nxt in graph[ny][nx]:
                    if nxt == color:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
    
    if color == 'W':
        white_power += cnt**2
    else:
        blue_power += cnt**2

for y in range(m):
    for x in range(n):
        if visited[y][x] == 0:
            bfs(y, x)

print(white_power, blue_power)