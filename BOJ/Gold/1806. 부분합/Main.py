n, s = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]*(n+1)
prefix[1] = arr[0]

for i in range(1, n):
    prefix[i+1] = arr[i] + prefix[i]

ans, pos, minus = int(1e9), 1, 0

while pos <= n:
    val = prefix[pos] - prefix[minus]

    if val < s:
        pos += 1
    else:
        ans = min(ans, pos-minus)
        minus += 1
        
if ans == int(1e9):
    print(0)
else:
    print(ans)