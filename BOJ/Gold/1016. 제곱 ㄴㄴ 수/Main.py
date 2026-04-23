a, b = map(int, input().split())
ans = 0
not_square = [False] * (b-a+1)

for i in range(2, int(b**0.5)+1):
    for j in range((a//(i**2))*(i**2), b+1, i**2):
        if a <= j and not not_square[j-a]:
            ans += 1
            not_square[j-a] = True

print(b-a-ans+1)