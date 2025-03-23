a = int(input())
b = int(input())
for i in range(int(a**0.5), int(b**0.5)+1):
    x = i*i
    if x >= a:
        print(x, end=" ")