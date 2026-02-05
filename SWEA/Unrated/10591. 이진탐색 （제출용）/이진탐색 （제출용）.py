for t in range(1, int(input())+1):
    p, a, b = list(map(int, input().split()))

    def find_idx(page):
        right, left, cnt = p, 1, 0
        for _ in range(10):
            mid = (right+left)//2
            if mid < page:
                left = mid
            elif mid > page:
                right = mid
            elif mid == page:
                break
            cnt += 1
        return cnt
    
    cnt = (find_idx(a), find_idx(b))
    ans = 'A' if cnt[0] < cnt[1] else ('B' if cnt[0] > cnt[1] else 0)
    print(f'#{t} {ans}')