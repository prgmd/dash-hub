import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
origin_area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

print(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)

cnt = 0
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    area = 0
    area += abs(x*(y2-y3)+x2*(y3-y)+x3*(y-y2))/2
    area += abs(x1*(y-y3)+x*(y3-y1)+x3*(y1-y))/2
    area += abs(x1*(y2-y)+x2*(y-y1)+x*(y1-y2))/2

    if area == origin_area:
        cnt += 1

print(cnt)