n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, 1<<n):
    total = 0
    for j in range(n):
        if i & (1<<j):
            total += arr[j]
    if total == s:
        cnt += 1
        
print(cnt)