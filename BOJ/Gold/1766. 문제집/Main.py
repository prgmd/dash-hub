import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    nums[a].append(b)
    degree[b] += 1

for num in nums:
    num.sort()

hq = []
for idx, d in enumerate(degree):
    if not idx:
        continue
    if not d:
        heapq.heappush(hq, idx)

result = []
while hq:
    now = heapq.heappop(hq)
    for nxt in nums[now]:
        degree[nxt] -= 1
        if not degree[nxt]:
            heapq.heappush(hq, nxt)
    result.append(now)

print(*result)