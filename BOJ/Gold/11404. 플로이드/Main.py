import sys
input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
city = [[int(1e9) for _ in range(n)] for _ in range(n)]

for i in range(n):
    city[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if city[a-1][b-1] > c:
        city[a-1][b-1] = c

for k in range(n):
    for y in range(n):
        for x in range(n):
            new_cost = city[y][k] + city[k][x]
            if city[y][x] > new_cost:
                city[y][x] = new_cost

for y in range(n):
    for x in range(n):
        if city[y][x] == int(1e9):
            city[y][x] = 0

for c in city:
    print(*c)