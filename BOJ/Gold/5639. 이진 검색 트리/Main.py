import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    idx = start + 1
    
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1
    
    post_order(start+1, idx-1)
    post_order(idx, end)
    print(root)

pre_order = []
while True:
    try:
        now = int(input())
        if not now:
            break
        pre_order.append(now)
    except ValueError:
        break

post_order(0, len(pre_order)-1)