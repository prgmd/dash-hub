line = input()
stack = []
postfix = ''

def priority(i):
    if i == '(':
        return 0
    elif i in '+-':
        return 1
    elif i in '*/':
        return 2
    elif i == ')':
        return 3

for l in line:
    if l == '(':
        stack.append(l)
    elif l == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            postfix += temp
    elif l in '+*-/':
        if stack:
            while stack and priority(stack[-1]) >= priority(l):
                postfix += stack.pop()
        stack.append(l)
    else:
        postfix += l

while stack:
    postfix += stack.pop()

print(postfix)