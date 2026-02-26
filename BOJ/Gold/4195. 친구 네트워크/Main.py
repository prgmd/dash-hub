import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())

def find(x):
    if x not in d:
        d[x] = x
    if d[x] != x:
        d[x] = find(d[x])
    return d[x]

def union(a, b):
    a = find(a)
    b = find(b)
    d[a] = b

def get_friend(a):
    root = find(a)
    cnt = 0
    for key in d:
        if find(d[key]) == root:
            cnt += 1
    return cnt

for _ in range(t):
    d = dict()
    for _ in range(int(input())):
        friend = list(input().split())
        friend.sort()
        a, b = friend[0], friend[1]
        union(a, b)
        print(get_friend(a))