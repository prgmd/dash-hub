import sys
input = sys.stdin.readline

for t in range(int(input())):
    h, w, n = map(int, input().split())
    n -= 1
    row = n%h+1
    col = n//h+1
    ans = str(row)
    if col < 10:
        ans += '0' + str(col)
    else:
        ans += str(col)
    print(ans)