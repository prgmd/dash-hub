import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    n = int(input())
    rgb = [list(map(int, input().split())) for _ in range(n)]
    ans = int(1e9)
    start = 3

    def bt(row, prev, total):
        nonlocal ans, start

        if ans <= total:
            return

        if row == n:
            if prev != start:
                ans = min(ans, total)
            return

        for x in range(3):
            if x != prev:
                total += rgb[row][x]
                row += 1
                bt(row, x, total)
                row -= 1
                total -= rgb[row][x]

    for x in range(3):
        start = x
        bt(1, x, rgb[0][x])

    print(ans)

solve()