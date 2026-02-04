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

visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1

# 너비 탐색으로 최단 거리 측정
def bfs():
    global answer

    q = deque()
    q.append((0, 0, 0))

    while q:
        # case : 0 - 벽 안 부숨 / case : 1 - 벽 부숨
        case, y, x = q.popleft()

        # n, m 도달시 최단 거리 비교하고 중단
        if (y, x) == (n-1, m-1):
            break

        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0 and visited[case][ny][nx] == -1:
                    visited[case][ny][nx] = visited[case][y][x] + 1
                    q.append((case, ny, nx))
                
                elif graph[ny][nx] == 1 and case == 0:
                    if visited[1][ny][nx] == -1:
                        visited[1][ny][nx] = visited[0][y][x] + 1
                        q.append((1, ny, nx))


# 블록 제거 없이 한 번 실행
bfs()

# 답 출력
answer = max(visited[0][n-1][m-1], visited[1][n-1][m-1])
print(answer)