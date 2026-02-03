from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
arr = deque()

for _ in range(6):
    arr.append(list(map(int, input().split())))

while True:
    if arr[0][0] == arr[2][0] and arr[1][0] == arr[3][0]:
        break
    arr.append(arr.popleft())

print(k * (arr[4][1]*arr[5][1] - arr[1][1]*arr[2][1]))