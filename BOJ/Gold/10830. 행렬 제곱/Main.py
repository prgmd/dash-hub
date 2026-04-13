import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def multi(mat1, mat2):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += mat1[i][k] * mat2[k][j]
            temp[i][j] %= 1000
    return temp

def power(mat, exp):
    if exp == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat

    half = power(mat, exp//2)

    if exp % 2:
        return multi(multi(half, half), mat)
    else:
        return multi(half, half)

result = power(a, b)

for row in result:
    print(*row)