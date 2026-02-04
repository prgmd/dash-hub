import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
graph.append([0] * (n+1))

for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

d = [(0, -1), (-1, 0)]

for y in range(1, n+1):
    for x in range(1, n+1):
        temp = graph[y][x]
        for dy, dx in d:
            ny, nx = y + dy, x + dx 
            temp += graph[ny][nx]
        graph[y][x] = temp - graph[y-1][x-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])