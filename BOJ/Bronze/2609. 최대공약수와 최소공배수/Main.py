n, m = map(int, input().split())
gcd = 1

if m > n:
    n, m = m, n

t_n, t_m = n, m
while True:
    if t_n % t_m == 0:
        gcd = t_m
        break
    else:
        t_n, t_m = t_m, t_n % t_m

print(gcd)
print(int(n*m/gcd))