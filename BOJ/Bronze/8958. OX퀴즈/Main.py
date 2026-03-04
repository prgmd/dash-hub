import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = input().rstrip()
    ans, temp = 0, 0

    for i in range(len(arr)):
        if arr[i] == 'O':
            temp += 1
            ans += temp
        else:
            temp = 0

    print(ans)