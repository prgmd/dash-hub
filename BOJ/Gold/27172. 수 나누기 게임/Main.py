import sys
input = sys.stdin.readline

n = int(input())
player = list(map(int, input().split()))
max_val = max(player)+1
is_exist = [False for _ in range(max_val)]
score = [0 for _ in range(max_val)]

for p in player:
    is_exist[p] = True

for p in player:
    for i in range(p*2, max_val, p):
        if is_exist[i]:
            score[p] += 1
            score[i] -= 1

for p in player:
    print(score[p], end= ' ')