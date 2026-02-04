from collections import defaultdict
from collections import deque

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

answer = 0

for item in range(1, len(items)):

    q = deque()
    q.append((item, m)) # 현재 위치와 남은 반경 입력

    visited = set()
    visited.add(item)

    item_total = items[item]

    while q:
        now, left_length = q.pop()
        if left_length < 0:
            continue

        for nxt, length in graph[now]:
            if length <= left_length and nxt not in visited:
                item_total += items[nxt]
                q.append((nxt, left_length-length))
                visited.add(nxt)
    
    # answer와 값 비교
    answer = max(item_total, answer)
print(answer)