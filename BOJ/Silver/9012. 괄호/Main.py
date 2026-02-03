for _ in range(int(input())):
    stack = []
    arr = input()
    is_error = False

    for a in arr:
        try:
            if a == '(':
                stack.append('(')
            else:
                stack.pop()
        except:
            is_error = True
            break
    
    if is_error:
        print('NO')
        continue

    if not stack:
        print('YES')
    else:
        print('NO')