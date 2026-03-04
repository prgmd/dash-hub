for _ in range(int(input())):
    r, s = input().split()
    ans = ''
    r = int(r)
    for i in range(len(s)):
        ans += s[i]*r
    print(ans)