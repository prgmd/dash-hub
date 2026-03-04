import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

def get_parent(x):
    while parent[curr] != curr:
        curr = parent[curr]
    while parent[x] != curr:
        nxt = parent[x]
        parent[x] = curr
        x = nxt
    return curr

def union_find(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def compare_parent(a, b):
    if get_parent(a) == get_parent(b):
        return False
    return True

arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key=lambda x:x[2])

ans = 0
for now in arr:
    a, b, c = now
    if compare_parent(a, b):
        union_find(a, b)
        ans += c
print(ans)