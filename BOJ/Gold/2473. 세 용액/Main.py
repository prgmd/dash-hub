import sys
input = sys.stdin.readline

n = int(input())
potions = list(map(int, input().split()))
potions.sort()

best = 1e11
ans = []

for i in range(n-2):
    l = i+1
    r = n-1

    while l < r:
        val = potions[i] + potions[l] + potions[r]
        
        if abs(val) < abs(best):
            best = val
            ans = [potions[i], potions[l], potions[r]]
        
        if val < 0:
            l += 1
        elif val > 0:
            r -= 1
        else:
            break

print(*ans)