a, b, c = map(int, input().split())

def square(exp):
    if exp == 1:
        return a
   
    half = square(exp//2)
    
    if exp % 2 == 0:
        return (half*half)%c
    else:
        return ((half*half)%c*a)%c
        
print(square(b)%c)