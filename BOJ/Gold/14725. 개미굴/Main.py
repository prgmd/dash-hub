import sys
input = sys.stdin.readline

trie = {}

def insert(lst):
    node = trie
    for word in lst:
        if word not in node:
            node[word] = {}
        node = node[word]
    node['#'] = True

def print_trie(cnt, node):
    for w in sorted(node.keys()):
        if w == '#':
            return
        print(f'{cnt*'--'}{w}')
        print_trie(cnt+1, node[w])
    return

def solve():
    n = int(input())
    for _ in range(n):
        cnt, *arr = input().split()
        cnt = int(cnt)
        insert(arr)  

    print_trie(0, trie)

solve()