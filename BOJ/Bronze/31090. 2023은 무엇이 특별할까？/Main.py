import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print('Good' if (n+1)%(int(str(n)[-2:]))==0 else 'Bye')