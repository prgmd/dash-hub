n = int(input())

def check_repeat(stack):
    i = 1
    while 2*i <= len(stack):
        if stack[-i:] == stack[-2*i:-i]:
            return True
        else:
            i += 1
    return False

def bt(n, stack):
    if check_repeat(stack):
        return
    
    if n == 0:
        print(''.join(map(str, stack)))
        exit()
    
    for x in [1, 2, 3]:
        stack.append(x)
        bt(n-1, stack)
        stack.pop()

    return

bt(n, [])