import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    n = find(a)
    m = find(b)
    if n > m:
        parent[n] = m
    else:
        parent[m] = n

for _ in range(m):
    cmd, a, b = map(int, input().split())
    
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')