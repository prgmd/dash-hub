from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

d = []
d.append([(0, 0),(0, 1),(0, 2),(0, 3)])
d.append([(0, 0),(0, 1),(0, 2),(1, 2)])
d.append([(0, 0),(0, 1),(0, 2),(1, 1)])
d.append([(0, 0),(0, 1),(0, 2),(1, 0)])
d.append([(0, 0),(0, 1),(0, 2),(-1, 2)])
d.append([(0, 0),(0, 1),(0, 2),(-1, 1)])
d.append([(0, 0),(0, 1),(0, 2),(-1, 0)])
d.append([(0, 0),(0, 1),(1, 1),(1, 2)])
d.append([(0, 0),(0, 1),(-1, 1),(-1, 2)])
d.append([(0, 0),(0, 1),(1, 0),(1, 1)])
d.append([(0, 0),(1, 0),(1, 1),(2, 1)])
d.append([(0, 0),(1, 0),(1, -1),(2, -1)])
d.append([(0, 0),(1, 0),(2, 0),(2, 1)])
d.append([(0, 0),(1, 0),(2, 0),(1, 1)])
d.append([(0, 0),(1, 0),(2, 0),(0, 1)])
d.append([(0, 0),(1, 0),(2, 0),(2, -1)])
d.append([(0, 0),(1, 0),(2, 0),(1, -1)])
d.append([(0, 0),(1, 0),(2, 0),(0, -1)])
d.append([(0, 0),(1, 0),(2, 0),(3, 0)])

def tetro(y, x):
    answer = 0
    for dist in d:
        temp = 0
        for dy, dx in dist:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                temp += graph[ny][nx]
            else:
                break
        answer = max(answer, temp)
    return answer

for y in range(n):
    for x in range(m):
        answer = max(answer, tetro(y, x))

print(answer)