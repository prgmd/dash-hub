for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n//3+1):
        ans += (n-i*3)//2+1
    print(ans)