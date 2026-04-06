n, r, c = map(int, input().split())
cnt = 0


def check(y, x, size):
    global cnt

    if size == 2:
        if y == r and x == c:
            print(cnt)
        elif y == r and x + 1 == c:
            print(cnt + 1)
        elif y + 1 == r and x == c:
            print(cnt + 2)
        elif y + 1 == r and x + 1 == c:
            print(cnt + 3)
        exit()
        return

    half = size // 2
    area = half * half

    if 0 <= r < y + half and 0 <= c < x + half:
        check(y, x, half)
    cnt += area

    if 0 <= r < y + half and x + half <= c < x + size:
        check(y, x + half, half)
    cnt += area

    if y + half <= r < y + size and 0 <= c < x + half:
        check(y + half, x, half)
    cnt += area

    if y + half <= r < y + size and x + half <= c < x + size:
        check(y + half, x + half, half)
    cnt += area


check(0, 0, 2**n)
