n = int(input())
digit = [0] * 10 
s, e = 1, n
point = 1

def count(num, p):
    while num > 0:
        digit[num % 10] += p
        num //= 10

while s <= e:
    while e % 10 != 9 and s <= e:
        count(e, point)
        e -= 1
    
    if e < s:
        break
    
    while s % 10 != 0 and s <= e:
        count(s, point)
        s += 1
        
    s //= 10
    e //= 10

    cnt = (e-s+1)*point
    for i in range(10):
        digit[i] += cnt
    point *= 10

print(*digit)