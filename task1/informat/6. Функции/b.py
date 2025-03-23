def power(a, n):
    x = a**n
    return x
a, n = map(float, input().split())
print(power(a, n))