from collections import defaultdict

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    d = defaultdict(list)

    for _ in range(e):
        i, j = map(int, input().split())
        d[i].append(j)
    
    s, g = map(int, input().split())
    ans = 0
    
    visited = [0] * (v+1)
    visited[s] = 1

    def dfs(now):
        global ans
        if now == g:
            ans = 1
            return
        for nxt in d[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                dfs(nxt)
    
    dfs(s)
    print(f'#{tc} {ans}')