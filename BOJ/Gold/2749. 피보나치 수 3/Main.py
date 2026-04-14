n = int(input())
p = 1500000
n %= p
fibo = [0] * p
fibo[1] = 1

for i in range(2, p):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000
    if i == n:
        break

print(fibo[n])