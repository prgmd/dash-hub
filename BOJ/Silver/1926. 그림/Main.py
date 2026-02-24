from collections import deque
from collections import defaultdict

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
graph = defaultdict(list)
visited = set()
connectCnt = 0

# 연결된 그래프 만들기
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            for dy, dx in d:
                ny = y + dy; nx = x + dx
                if (y, x) not in graph.keys():
                    graph[(y, x)]
                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1:
                    graph[(y, x)].append((ny, nx))

# bfs 함수
def bfs(start, graph, cnt):
    q = deque([start])
    visited.add(start)

    while q:
        now = q.popleft()
        for next in graph[now]:
            if next not in visited:
                cnt += 1
                q.append(next)
                visited.add(next)

    return cnt

maxCnt = 0
for start in graph:
    if start not in visited:
        connectCnt += 1
        maxCnt = max(maxCnt, bfs(start, graph, 1))

print(connectCnt)
print(maxCnt)