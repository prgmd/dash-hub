import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((int(age), i, name))

arr.sort()
for a in arr:
    print(a[0], a[2])