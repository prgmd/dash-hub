import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parents = [i for i in range(n)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA == rootB:
        return True
    
    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB
    
    return False

ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        ans = i+1
        break

print(ans)