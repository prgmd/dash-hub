from collections import deque

n = int(input())
nodes = [[] for _ in range(n)]
nums = [1] * n

def gcd(m, n):
  if m < n:
    m, n = n, m

  while True:
    r = m % n
    if not r:
      return n
    m, n = n, r

for _ in range(n-1):
  a, b, p, q = map(int, input().split())
  nodes[a].append((b, p, q/p))
  nodes[b].append((a, q, p/q))

def bfs():
  dq = deque()
  dq.append((0, 1))
  visited = [True] + [False] * (n-1)
  total = 1

  while dq:
    now, weight = dq.popleft()
    for nxt, val, ratio in nodes[now]:
      if not visited[nxt]:
        visited[nxt] = True
        total *= val
        nums[nxt] *= ratio*weight
        dq.append((nxt, weight*ratio))

  for i in range(n):
    nums[i] = round(nums[i]*total)

bfs()

k = nums[0]
for i in range(1, n):
  k = gcd(k, nums[i])

for i in range(n):
  nums[i] = int(nums[i]/k)

print(*nums)