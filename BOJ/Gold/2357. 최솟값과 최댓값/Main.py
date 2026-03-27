import sys
input = sys.stdin.readline

n, m = map(int, input().split())
original = [int(input()) for _ in range(n)]
tree = [0]*(4*n)
value = [int(1e9), 0]

def set_tree(start, end, node):
    if start == end:
        tree[node] = (original[start], original[start])
        return tree[node]
    
    mid = (start + end) // 2
    left = set_tree(start, mid, node*2)
    right = set_tree(mid+1, end, node*2+1)
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]

set_tree(0, n-1, 1)

def find_node(start, end, node, left, right):
    if left > end or right < start:
        return
    
    if left <= start and right >= end or start == end:
        value[0] = min(value[0], tree[node][0])
        value[1] = max(value[1], tree[node][1])
        return
    
    mid = (start + end) // 2
    find_node(start, mid, node*2, left, right)
    find_node(mid+1, end, node*2+1, left, right)

def solve():
    set_tree(0, n-1, 1)

    for _ in range(m):
        a, b = map(int, input().split())
        value[0], value[1] = int(1e9), 0
        find_node(0, n-1, 1, a-1, b-1)
        print(*value)

solve()