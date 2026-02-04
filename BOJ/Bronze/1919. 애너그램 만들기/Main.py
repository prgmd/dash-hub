from collections import defaultdict
a = list(input())
b = list(input())
d = defaultdict(int)

for i in a:
    d[i] += 1

for i in b:
    d[i] -= 1

print(sum(list(map(abs, d.values()))))