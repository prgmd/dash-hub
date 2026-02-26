import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(i, j):
    a = find(i)
    b = find(j)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i, g in enumerate(graph):
    for j, val in enumerate(g):
        if val == 1:
            union(i, j)

ans = 'YES'
root = find(route[0]-1)
for i in range(1, m):
    if find(route[i]-1) != root:
        ans = 'NO'
        break

print(ans)