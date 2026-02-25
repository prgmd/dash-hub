n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]

# 해당 크기 안에 같은 수로 채워졌는지 체크
def is_paper(y, x, n):
    color = graph[y][x]
    for i in range(n):
        for j in range(n):
            if graph[y+i][x+j] != color:
                return False
    cnt[color+1] += 1
    return True

# 종이 구하기 함수
def get_paper(y, x, n):
    # 만약 종이 크기가 1이라면 직접 더함
    if n == 1:
        cnt[graph[y][x]+1] += 1
        return

    # 만약 n 크기의 종이가 같은 수를 만족하지 않는다면
    if not is_paper(y, x, n):
        # 종이를 9개로 쪼개서
        d = n//3
        for i in range(0, n, d):
            for j in range(0, n, d):
                # 종이 구하기 함수에 다시 넣음
                get_paper(y+i, x+j, d)

get_paper(0, 0, n)
for c in cnt:
    print(c)