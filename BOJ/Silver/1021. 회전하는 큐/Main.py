from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))

numbers = [i for i in range(1, n+1)]
q = deque(numbers)

def find_idx(n):
    for idx, val in enumerate(q):
        if val == n:
            return idx

ans = 0
for now in pos:
    if now == q[0]:
        q.popleft()
    else:
        while now != q[0]:
            idx = find_idx(now)
            if idx <= len(q) - idx:
                temp = q.popleft()
                q.append(temp)
            else:
                temp = q.pop()
                q.appendleft(temp)
            ans += 1
        q.popleft()

print(ans)