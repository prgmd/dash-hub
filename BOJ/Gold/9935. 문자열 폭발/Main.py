words = input()
bomb = input()
n = len(bomb)
stack = []

for w in words:
    stack.append(w)
    if w == bomb[-1] and len(stack) >= n:
        if ''.join(stack[-n:]) == bomb:
            for _ in range(n):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')