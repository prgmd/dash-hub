import sys
input = sys.stdin.readline

from collections import deque

# 변수 설정
n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = int(1e9)
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 블록 좌표 체크
blocks = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            blocks.append((y, x))

# 너비 탐색으로 최단 거리 측정
def bfs():
    global answer

    q = deque()
    q.append((0, 0, 1))

    visited = set()
    visited.add((0, 0))

    while q:
        y, x, dist = q.popleft()

        # n, m 도달시 최단 거리 비교하고 중단
        if (y, x) == (n-1, m-1):
            answer = min(answer, dist)
            break

        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited and graph[ny][nx] == 0:
                q.append((ny, nx, dist+1))
                visited.add((ny, nx))

# 블록 제거 없이 한 번 실행
bfs()

# 제외할 블록 선정
for block in blocks:
    y, x = block
    graph[y][x] = 0
    bfs()
    graph[y][x] = 1

# 답 출력
print(-1 if answer == int(1e9) else answer)