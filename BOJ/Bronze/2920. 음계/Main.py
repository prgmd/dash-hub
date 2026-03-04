arr = list(map(int, input().split()))
ascending = sorted(arr)
descending = sorted(arr, reverse=True)

if arr == ascending:
    print('ascending')
elif arr == descending:
    print('descending')
else:
    print('mixed')