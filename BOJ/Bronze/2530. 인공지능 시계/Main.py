h, m, s = map(int, input().split())
s += int(input())

while h > 23 or m > 59 or s > 59:
    if s >= 60:
        m += s // 60
        s %= 60
    elif m >= 60:
        h += m // 60
        m %= 60
    elif h >= 24:
        h -= 24

print(h, m, s)