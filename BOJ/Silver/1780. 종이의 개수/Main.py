n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]

def is_paper(y, x, n):
    color = graph[y][x]
    for i in range(n):
        for j in range(n):
            if graph[y+i][x+j] != color:
                return False
    cnt[color+1] += 1
    return True

def get_paper(y, x, n):
    if not is_paper(y, x, n):
        d = n//3
        for i in range(0, n, d):
            for j in range(0, n, d):
                get_paper(y+i, x+j, d)

get_paper(0, 0, n)
for c in cnt:
    print(c)