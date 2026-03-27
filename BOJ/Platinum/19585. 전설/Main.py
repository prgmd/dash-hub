import sys
input = lambda: sys.stdin.readline().rstrip()

trie = {}

def insert(word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = True

c, n = map(int, input().split())
colors = [input() for _ in range(c)]
nicknames = [input() for _ in range(n)]
teams = [input() for _ in range(int(input()))]

def search(word):
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '#' in node

for color in colors:
    for nick in nicknames:
        insert(color+nick)

for team in teams:
    if search(team):
        print('Yes')
    else:
        print('No')