import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
start, end = lines[0][0], lines[0][1]

ans = 0

for x, y in lines:
    if x > end:
        ans += abs(end-start)
        start, end = x, y
    elif start <= x <= end and y > end:
        end = y

print(ans + abs(end-start))