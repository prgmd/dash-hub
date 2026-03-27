import sys
input = lambda: sys.stdin.readline().rstrip()

color_trie = {}
nick_trie = {}

def insert(word, trie, type):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node[type] = True

def search(word):
    node = color_trie
    for idx, char in enumerate(word):
        if char not in node:
            if '.' in node and char in nick_trie:
                node = nick_trie[char]
            else:
                return False
        else:
            if '.' in node:
                if nick_search(word[idx-1:]):
                    return True
            node = node[char]
    return '#' in node

def nick_search(word):
    node = nick_trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '#' in node

def solve():
    c, n = map(int, input().split())
    for _ in range(c):
        insert(input(), color_trie, '.')

    for _ in range(n):
        insert(input(), nick_trie, '#')

    for _ in range(int(input())):    
        print('Yes' if search(input()) else 'No')

solve()