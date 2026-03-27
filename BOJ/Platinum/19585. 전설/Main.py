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
    for char in word:
        if char not in node:
            if '.' in node and char in nick_trie:
                node = nick_trie[char]
            else:
                return False
        else:
            node = node[char]
    return '#' in node

def solve():
    c, n = map(int, input().split())
    colors = [input() for _ in range(c)]
    nicknames = [input() for _ in range(n)]
    teams = [input() for _ in range(int(input()))]

    for color in colors:
        insert(color, color_trie, '.')
    
    for nick in nicknames:
        insert(nick, nick_trie, '#')
    
    for team in teams:
        print('Yes' if search(team) else 'No')

solve()