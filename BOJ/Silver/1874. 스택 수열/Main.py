import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
num = 1

for _ in range(n):
    now = int(input())
    
    while num <= now:
        stack.append(num)
        answer.append('+')
        num += 1
    
    if stack[-1] == now:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit()

for a in answer:
    print(a)