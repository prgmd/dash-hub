import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    pitagoras = [a, b, c]
    pitagoras.sort()

    if pitagoras[0]**2 + pitagoras[1]**2 == pitagoras[2]**2:
        print('right')
    else:
        print('wrong')