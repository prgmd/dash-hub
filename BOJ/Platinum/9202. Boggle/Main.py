import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

trie = {}
score_board = [0, 0, 0, 1, 1, 2, 3, 5, 11]

def set_trie(word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['#'] = word

def find_word(y, x, node):
    if '#' in node:
        found.add(node['#'])

    for dy, dx in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4 and not visited[ny][nx]:
            nxt = board[ny][nx]
            if nxt in node:
                visited[ny][nx] = True
                find_word(ny, nx, node[nxt])
                visited[ny][nx] = False
    return
                    
def solve():
    for _ in range(int(input())):
        set_trie(input())
    input()

    for _ in range(int(input())):
        global board, found, visited
        board = [list(input()) for _ in range(4)]
        found = set()
        visited = [[False] * 4 for _ in range(4)]

        for y in range(4):
            for x in range(4):
                if board[y][x] in trie:                    
                    visited[y][x] = True
                    find_word(y, x, trie[board[y][x]])
                    visited[y][x] = False

        score = 0
        longest = ''
        for word in found:
            score += score_board[len(word)]
            if len(longest) < len(word) or len(longest) == len(word) and longest > word:
                longest = word

        print(score, longest, len(found))
        input()

solve()