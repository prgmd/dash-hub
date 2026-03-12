from collections import deque

n, m = map(int, input().split())
students = dict()
degree = [1] + [0]*(n)

for _ in range(m):
    a, b = map(int, input().split())
    if a not in students:
        students[a] = []
    students[a].append(b)
    degree[b] += 1

q = deque()
for idx, d in enumerate(degree):
    if not d:
        q.append(idx)

while q:
    now = q.popleft()
    if now in students:
        for nxt in students[now]:
            degree[nxt] -= 1
            if not degree[nxt]:
                q.append(nxt)
    print(now, end=' ')