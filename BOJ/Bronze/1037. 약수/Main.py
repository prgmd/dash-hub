n = int(input())
yaksu = list(map(int, input().split()))
cnt = 2
ans = int(1e9)
while cnt < 1000001:
    is_odd = True
    for y in yaksu:
        if y != cnt and cnt % y == 0:
            continue
        else:
            is_odd = False
            break
    if is_odd:
        print(cnt)
        break
    cnt += 1