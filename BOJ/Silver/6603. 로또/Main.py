import sys
input = sys.stdin.readline

while True:
    k, *s = list(map(int, input().split()))

    if k == 0:
        exit()

    ans = []
    for i in range(1<<k):
        cnt = 0
        temp = []
        for j in range(k):
            if i & (1<<j):
                cnt += 1
                temp.append(s[j])
        if cnt == 6:
            ans.append(temp)
    
    ans.sort()
    for a in ans:
        print(*a)
    print()
