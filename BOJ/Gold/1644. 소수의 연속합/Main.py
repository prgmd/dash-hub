n = int(input())
board = [0 for _ in range(n+1)]
is_prime = [True for _ in range(n+1)]
prime = []

for i in range(2, n+1):
    if is_prime[i]:
        prime.append(i)
        is_prime[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))

s, e, ans = 0, 0, 0
total_prime = len(prime)

while e < total_prime:
    if s == e:
        total = prime[s]
    else:
        total = sum(prime[s:e+1])
    
    if total < n:
        e += 1
    elif total > n:
        s += 1
    elif total == n:
        ans += 1
        s += 1

print(ans)