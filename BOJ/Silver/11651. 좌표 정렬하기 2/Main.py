arr = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x, y))

answer = sorted(sorted(arr), key = lambda x : x[1])
for a in answer:
    print(*a)