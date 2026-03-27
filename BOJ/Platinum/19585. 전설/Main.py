import sys
input = lambda: sys.stdin.readline().rstrip()

color_trie = {}
nicknames = set()

def insert(word, trie):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True

def search(word):
    node = color_trie
    for i in range(len(word)):
        char = word[i]
        if '#' in node:
            if word[i:] in nicknames:
                return True
        if char not in node:
            return False
        node = node[char]
    return False

def solve():
    c, n = map(int, input().split())
    for _ in range(c):
        insert(input(), color_trie)

    for _ in range(n):
        nicknames.add(input())

    teams = [input() for _ in range(int(input()))]
    for team in teams:
        print('Yes' if search(team) else 'No')

solve()