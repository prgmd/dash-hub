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

def search(word):
    node = trie
    cnt = 0
    for idx, char in enumerate(word):
        if len(node) >= 2:
            cnt += 1
        node = node[char]
    return cnt

def solve():
    words = []
    N = int(input())
    for _ in range(N):
        word = input()
        words.append(word)
        insert(word)

    ans = 0
    for word in words:
        ans += search(word)
    print(f'{ans/N:.2f}')

try:
    while True:
        trie = {'#':True}
        solve()
except Exception:
    exit()