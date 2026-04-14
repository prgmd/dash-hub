import sys
input = sys.stdin.readline

n = int(input())
menu = sorted(list(map(int, input().split())))
m = 1000000007

pow = [1] * n
for i in range(1, n):
    pow[i] = (pow[i-1] * 2) % m

ans = 0
for i in range(n//2):
    left, right = i, n-1-i
    exp = pow[right] - pow[left]
    ans = (ans + (menu[right] - menu[left]) * exp) % m

print(ans)