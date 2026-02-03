from collections import deque

for _ in range(int(input())):
    p = input()
    n = int(input())
    temp = input()
    if temp == '[]':
        arr = deque()
    else:
        arr = deque(temp[1:len(temp)-1].split(','))
    is_front = True
    is_error = False

    for order in p:
        try:
            if order == 'R':
                is_front = not is_front
            else:
                if is_front:
                    arr.popleft()
                else:
                    arr.pop()
        except:
            is_error = True
            break
          
    if is_error:
        print('error')
    else:
        if not is_front:
            arr.reverse()
        print('[', end = '')
        if arr:
            for i, a in enumerate(arr):
                print(a, end = '')
                if i != len(arr)-1:
                    print(',', end = '')
        print(']')