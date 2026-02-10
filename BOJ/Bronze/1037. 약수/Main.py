n = int(input())
yaksu = list(map(int, input().split()))
print(2 if n == 1 and yaksu[0] == 1 else max(yaksu)*min(yaksu))