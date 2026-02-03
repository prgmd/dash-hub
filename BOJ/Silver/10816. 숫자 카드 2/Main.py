from collections import defaultdict

n = int(input())
num_card = list(map(int, input().split()))
d = defaultdict(int)
for nc in num_card:
    d[nc] += 1

m = int(input())
answer = []
match_card = list(map(int, input().split()))
for mc in match_card:
    answer.append(d[mc])

print(*answer)