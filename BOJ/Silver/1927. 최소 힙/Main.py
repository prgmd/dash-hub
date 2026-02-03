import heapq
import sys
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    now = int(input())
    
    if now == 0:
        print(heapq.heappop(q) if q else 0)
    else:
        heapq.heappush(q, now)