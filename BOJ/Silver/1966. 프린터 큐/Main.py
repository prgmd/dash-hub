from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = map(int, input().split())
    q = deque()
    for idx, imp in enumerate(importance):
        q.append((imp, idx))

    now = q.popleft()
    cnt = 1

    while q:
        if now[0] < max(q)[0]:
            q.append(now)
        else:
            if now[1] == m:
                break
            cnt += 1
        now = q.popleft()

    print(cnt)